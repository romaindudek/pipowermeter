#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from pipowermeter.package.functions import *
from pipowermeter.package.output import OutputMeasure, mySettings


print(f"{bcolors.FAIL}WARNING : I am the daemon !\nYou should not launch me, use \"./setup.py\" instead...\nPlease press ctrl+c within 20 seconds to abort{bcolors.ENDC}")
time.sleep(20)

while True:
    if mySettings.record == False:
        output = OutputMeasure()
        output.print_measure()
        output.line_measure()
    else:
        print("Not recording")
    time.sleep(mySettings.timeDelay)