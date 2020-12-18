#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys



class AppInfos():
    """
    Base Information and printing instructions
    """

    def __init__(self):
        self.app_name = "Pi Power-meter"
        self.version = "0.0.1"
        self.sep  =  "###########################"
        self.hstr = """
> Usage : ./setup install [option]

> options :

    install     : install the application (questions will be asked)
    uninstall   : Uninstall the application (wont remove data directory)
    trash       : Uninstall the application and delete data directory

    start       : Start new measurement project
    stop        : Stop measurement project
        
        """
        self.system = os.uname()

    def prtHeader(self):
        print("%s\n%s v %s\n%s" %(self.sep, self.app_name, self.version, self.sep))
        if(self.system.machine != "arm"):
            q = input(f"{bcolors.WARNING}Warning:  {self.system.sysname} / {self.system.machine} is probably not a Raspberry pi, do you want to continue (y/n)? {bcolors.ENDC}")
            if (q != "y"):
                print("Setup is stopped")
                sys.exit()
        else:
            print(f"{bcolors.OKGREEN}self.system.sysname self.system.machine{bcolors.ENDC}")

class Installation():
    def __init__(self):
        self.init = True


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


    


