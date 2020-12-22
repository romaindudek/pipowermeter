#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import datetime
import requests
from .functions import *

from .settings import MySettings, propsArray

class Installation:
    """
    Functions used for installation and desinstallation purposes
    """

    def __init__(self):
        AppInit().sys_check()
        self.service_present = True if subprocess.run(["sudo apt list --installed 2>/dev/null | grep pipowermeter"], shell=True).returncode != 1 else False
    
    def install(self):
        mySettings = MySettings()
        for prop in propsArray:
            if prop['name'] != 'record':
                propVal = getattr(mySettings, prop['name'])
                q = input(f"\n> The setting {bcolors.OKGREEN}\"{prop['name']}\"{bcolors.ENDC} is set to {bcolors.OKGREEN}\"{propVal}\"{bcolors.ENDC}, do you want to overwrite it (y/n)? ")
                if q == 'y':
                    q = input("  Please enter the new value : ")
                    #q =q.replace(" ", "_")
                    mySettings.set_local(prop['name'], q)
                    print(f"  Setting \"{prop['name']}\" has been set to {bcolors.OKBLUE}\"{q}\"{bcolors.ENDC}")

    def uninstall(self):
        print("Start Uninstalling !")

    def trash(self):
        print("Start Trashing !")