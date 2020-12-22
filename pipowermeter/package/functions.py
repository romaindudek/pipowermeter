#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import pickle

def pickle_get_or_set(filePath, varSet):
    """
    Get or sets datas in a pickle file,
    creates it if it is not present.
    """
    if os.path.isfile(filePath) :
        with open(filePath, 'rb') as f:
            varSet = pickle.load(f)
        return {"varSet": varSet, "action": "get"}
    else:
        pickle_wr(filePath, varSet)
        return {"varSet": varSet, "action": "set"}

def pickle_wr(filePath, varSet):
    """
    Write a pickle file
    """
    with open(filePath, 'wb') as f:
        pickle.dump(varSet, f)

class AppInit:
    """
    Base Information and printing instructions
    """

    def __init__(self):
        self.app_name = "Pi PowerMeter"
        self.version = "0.0.1"
        self.sep  =  "###########################"
        self.hstr = """
* Usage : ./setup.py [option]

* Available options :

    install     : Install the application (questions will be asked)
    uninstall   : Uninstall the application (wont remove data directory)
    trash       : Uninstall the application and delete data directory

    start       : Start new measurement project
    stop        : Stop measurement project"""
        self.system = os.uname()

    def prt_header(self):
        """
        Print header
        """
        print(f"{bcolors.HEADER}%s\n%s v %s\n%s{bcolors.ENDC}" %(self.sep, self.app_name, self.version, self.sep))
        
    def sys_check(self):
        """
        Print system information and ask for action if system is not Raspberry pi
        """
        if("arm" not in self.system.machine):
            q = input(f"{bcolors.WARNING}Warning:  {self.system.sysname} / {self.system.machine} is probably not a Raspberry pi, do you want to continue (y/n)? {bcolors.ENDC}")
            if (q != "y"):
                print("Setup is stopped")
                sys.exit()
        else:
            print(f"{bcolors.OKGREEN}{self.system.sysname} / {self.system.machine} seems to be a Raspberry Pi !{bcolors.ENDC}")




class Exec:
    """
    Functions used for execution
    """
    def __init__(self):
        pass
    
    def m_start(self):
        print("Starting measurement")

    def m_stop(self):
        print("Stopping measurement")

class Questions:
    """
    functions used for interactions
    """
    def __init__(self, q):
        self.q = q
    
class ServiceManage:

    def __init__(self):
        self.serviceName = "pipowermeter"
        self.isActive = self.check_service_property("ActiveState")
        self.isLoaded = self.check_service_property("LoadState")
    
    def check_service_property(self, propName):
        ret = subprocess.run(["systemctl", "show", self.serviceName, "--property=" + propName], capture_output=True)
        ret = self.active_state_from_stdout(ret.stdout, propName)
        return ret

    def active_state_from_stdout(self, stdoutStr, propName):
        ret = stdoutStr.decode("utf-8")
        rem = propName + "="
        ret = ret.replace(rem, "").replace("\n", "")
        if (ret == "active" or ret == "loaded"):
            return True
        else:
            return False



class bcolors:
    """
    Used for coloring text if needed
    """
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


    


