#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .settings import MySettings
from .measurement import PowerMeasure

my_settings = MySettings()

class OutputMeasure:
    
    def __init__(self):
        self.measure = PowerMeasure()

    def print_measure(self):
        print(f"Device name: {my_settings.deviceName} | Location: {my_settings.location} | Power: {self.measure.power}W")

    def line_measure(self):
        return f"{my_settings.deviceName},{my_settings.location},{self.measure.power};\\n"


