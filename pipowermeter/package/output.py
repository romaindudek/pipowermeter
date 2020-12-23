#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import datetime
import requests

from .settings import MySettings
from .measurement import PowerMeasure
from csv import writer

mySettings = MySettings()

# Read or Write in csv files
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj, delimiter=mySettings.csvSep)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

class OutputMeasure:
    
    def __init__(self):
        self.measure = PowerMeasure()
        self.currentDT = datetime.datetime.now()
        self.w = self.get_weather_cast()

    def print_measure(self):
        dt = self.currentDT.strftime("%Y/%m/%d at %H:%M:%S")
        print(f"Time: {dt} | Device name: {mySettings.deviceName} | Location: {mySettings.location} | Power: {self.measure.power}W | Consumption: {round(self.measure.power/3600*int(mySettings.timeDelay),3)}Wh | Temperature : {self.w['temp']}°C | Wind : {self.w['wind']}Km/h | Clouds : {self.w['clouds']}%")

    def line_measure(self):
        dt = self.currentDT.strftime("%Y%m%d%H%M%S")
        readableDT = self.currentDT.strftime("%Y/%m/%d at %H:%M:%S")
        value = [dt,mySettings.deviceName,mySettings.location,readableDT,self.measure.power, round(self.measure.power/3600*int(mySettings.timeDelay),3),self.w['temp'],self.w['wind'],self.w['clouds']]
        append_list_as_row(mySettings.datas + f"{mySettings.projectName}.csv", value)
        return value
    
    def get_weather_cast(self):
        q = f"api.openweathermap.org/data/2.5/weather?q={mySettings.location}&units=metric&appid={mySettings.apiKey}"
        try:
            response = requests.get(f"http://{q}")
            currentTemperature = response.json()['main']['temp']
            currentWind = round(response.json()['wind']['speed']*3.6, 0)
            currentCloudiness = round(response.json()['clouds']['all'])
            if response.status_code == 200:
                return {"temp":currentTemperature,"wind":currentWind,"clouds":currentCloudiness}
            else:
                return {"temp":None,"wind":None,"clouds":None}
        except Exception as e:
            print("Exception : " + str(e))
            return {"temp":None,"wind":None,"clouds":None}

