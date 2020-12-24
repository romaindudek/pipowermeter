#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import datetime
import requests

from .functions import *
from .settings import MySettings
from .properties import appProperties
from .service import ServiceManage

class Installation:
    """
    Functions used for installation and desinstallation purposes
    """

    def __init__(self):
        AppInit().sys_check()
        self.service_present = True if subprocess.run(["sudo apt list --installed 2>/dev/null | grep pipowermeter"], shell=True).returncode != 1 else False
    
    def install(self):
        mySettings = MySettings()
        for prop in appProperties.propsArray:
            if prop['name'] != 'record':
                propVal = getattr(mySettings, prop['name'])
                q = input(f"\n> The setting {bcolors.OKGREEN}\"{prop['name']}\"{bcolors.ENDC} is set to {bcolors.OKGREEN}\"{propVal}\"{bcolors.ENDC}, do you want to overwrite it (y/n)? ")
                if q == 'y':
                    q = input("  Please enter the new value : ")
                    #q =q.replace(" ", "_")
                    mySettings.set_local(prop['name'], q)
                    print(f"  Setting \"{prop['name']}\" has been set to {bcolors.OKBLUE}\"{q}\"{bcolors.ENDC}")
        serv = ServiceManage("pipowermeter")
        print(f"\n  The service statuses are :\n  {bcolors.OKBLUE}Loaded : {serv.is_loaded} / Active : {serv.is_active}\n{bcolors.ENDC}")
        if not serv.is_loaded or not serv.is_active:
            q = input(f"> Do you want to {bcolors.OKGREEN}install/reinstall{bcolors.ENDC} the service (y/n)? ")
            if q == "y":
                serv.CheckRights() # Exits if not Super User
                # Install the daemon
                service_file_path = f"{mySettings.baseDir}{os.sep}pipowermeter"
                fin = open(f"{service_file_path}.txt", "rt")
                fout = open(f"{service_file_path}.service", "wt")
                for line in fin:
                    fout.write(line.replace("ExecStart=/usr/bin/python3", f"ExecStart=/usr/bin/python3 {service_file_path}.py"))
                    print('.', end='')
                print()
                print(f"  Fichier {bcolors.OKGREEN}{service_file_path}.service{bcolors.ENDC} créé")
                fin.close()
                fout.close()

        print(f"\n> Congratulations, Pi PowerMeter is installed... Measurements will be stored in {bcolors.OKGREEN}{mySettings.datas}{mySettings.projectName}.csv{bcolors.ENDC}")
        print(messages.COMPLETEINSTALL)

    def uninstall(self):
        print("Start Uninstalling !")

    def trash(self):
        print("Start Trashing !")


