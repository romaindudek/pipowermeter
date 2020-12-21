#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import datetime
 
currentDT = datetime.datetime.now()

from .settings import MySettings
from .measurement import PowerMeasure

mySettings = MySettings()

# Read or Write in csv files
from csv import writer

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


class OutputMeasure:
    
    def __init__(self):
        self.measure = PowerMeasure()

    def print_measure(self):
        print(f"Device name: {mySettings.deviceName} | Location: {mySettings.location} | Power: {self.measure.power}W")

    def line_measure(self):
        dt = currentDT.strftime("%Y%m%d%H%M%S")
        value = [mySettings.deviceName,mySettings.location,dt,self.measure.power]
        append_list_as_row(mySettings.datas + "test.csv", value)
        return value


