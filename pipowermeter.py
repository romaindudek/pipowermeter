#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from pipowermeter.package.messages import messages
from pipowermeter.package.functions import *
from pipowermeter.package.output import OutputMeasure, mySettings


print(f"{bcolors.FAIL}{messages.DEVIL}WARNING : I am the daemon !\nThou shalt not launch me this way unless \nyou are a developper, a maintainer or a fool...\nUse \"./setup.py\" instead, and follow the instructions...\nPlease press ctrl+c asap to abort{bcolors.ENDC}")
time.sleep(15)

while True:
    if mySettings.record == True:
        output = OutputMeasure()
        output.print_measure()
        output.line_measure()
    else:
        print("Not recording")
    mySettings.refresh()
    time.sleep(int(mySettings.timeDelay))