#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import datetime
import requests
import os
import filecmp
import shutil
import subprocess

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
                src = f"{service_file_path}.service"
                dst = f"/etc/systemd/system/pipowermeter.service"
                if os.path.exists(dst):
                    print(f"Destination file {dst} exists, use \"./setup.py uninstall\" before trying again")
                else:
                    try:
                        shutil.copyfile(src, dst)
                        print(f"{src} copyed to {bcolors.OKGREEN}{dst}{bcolors.ENDC}")
                        try :
                            os.system("sudo systemctl enable pipowermeter.service")
                            print(f"{bcolors.OKGREEN}Service is enabled{bcolors.ENDC}")
                            os.system("sudo systemctl start pipowermeter.service")
                            print(f"{bcolors.OKGREEN}Service is started{bcolors.ENDC}")
                        except Exception as e:
                            print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
                    except Exception as e:
                        print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")


        print(f"\n> Congratulations, Pi PowerMeter is installed... Measurements will be stored in {bcolors.OKGREEN}{mySettings.datas}{mySettings.projectName}.csv{bcolors.ENDC}")
        if mySettings.record:
            print(messages.COMPLETEINSTALLRECORD)
        else:    
            print(messages.COMPLETEINSTALL)

    def uninstall(self):
        mySettings = MySettings()
        service_file_path = f"{mySettings.baseDir}{os.sep}pipowermeter"
        print("Uninstalling Pi PowerMeter")
        try :
            os.system(f"sudo rm {service_file_path}.service")
            print(f"{bcolors.OKGREEN}{service_file_path}.service is removed{bcolors.ENDC}")
            os.system("sudo systemctl stop pipowermeter.service")
            print(f"{bcolors.OKGREEN}Service is stopped{bcolors.ENDC}")
            os.system("sudo systemctl disable pipowermeter.service")
            print(f"{bcolors.OKGREEN}Service is disabled{bcolors.ENDC}")
            os.system(f"sudo rm /etc/systemd/system/pipowermeter.service")
            print(f"{bcolors.OKGREEN}Pi PowerMeter is uninstalled.{bcolors.ENDC}")
        except Exception as e:
            print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")


    def trash(self):
        print("Start Trashing !")


