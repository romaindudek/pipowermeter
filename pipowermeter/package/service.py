# -*- coding: utf-8 -*-

import os
import glob
import re
import subprocess
import sys

from .messages import *

class ServiceManage:

    def __init__(self, serviceName):
        self.service_name = serviceName
        self.is_active = self.check_service_property("ActiveState")
        self.is_loaded = self.check_service_property("LoadState")
    
    def check_service_property(self, prop_name):
        ret = subprocess.run(["systemctl", "show", self.service_name, "--property=" + prop_name], capture_output=True)
        ret = self.active_state_from_stdout(ret.stdout, prop_name)
        return ret

    def active_state_from_stdout(self, stdout_str, prop_name):
        ret = stdout_str.decode("utf-8")
        rem = prop_name + "="
        ret = ret.replace(rem, "").replace("\n", "")
        if (ret == "active" or ret == "loaded"):
            return True
        else:
            return False

    def CheckRights(self):
        try:
            # Open the file "/etc/service" can only be done with Super User rights
            with open(f"/etc/service", "w") as fp: 
                pass
        except IOError :
            print()
            print(messages.WARNING)
            print()
            print(f"To install the service, this script has to be executed as Super User,\ntry :  {bcolors.OKGREEN}\"sudo ./setup.py install\"{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Exiting setup.py... Please try again. ;-){bcolors.ENDC}")
            print()
            print()
            sys.exit()


class ManageService:
    """
    Manage service from it's name
    """
    def __init__(self, serviceName):
        self.CheckRights()
        self.service_name = serviceName
        self.service_present = True if subprocess.run([f"sudo apt list --installed 2>/dev/null | grep {serviceName}"], shell=True).returncode != 1 else False
        self.service_in_rcd = True if len(self.checkrcd()) > 0 else False

    def checkrcd(self):
        """
        Vérifie qu'un fichier service du type ***service est bien présent dans un des répertoires /etc/rc*
        Renvoie le chemin complet vers ce(s) fichier(s)
        """
        # list the dirs
        dirs = []
        service_list = []
        for direct in glob.glob( os.sep + 'etc' + os.sep +'rc*'):
            dirs.append(direct)
        
        for dir in dirs:
            path = f"{dir}{os.sep}*{self.service_name}"
            for file in glob.glob(path):
                service_list.append(file)
        return service_list



    def modifConfigs(self):
        conf_file_1 = '/etc/pipowermeter.conf'
        with open(conf_file_1) as f:
            data = f.read()
            data = re.sub(r'\n#pipowermeter-device.+\n', '\npipowermeter-device    = /dev/pipowermeter\n', data )
            data = re.sub(r'\n#interval.+\n', '\ninterval        = 4\n', data )
            data = re.sub(r'\n#realtime.+\n', '\nrealtime        = yes\n', data )
            data = re.sub(r'\n#priority.+\n', '\npriority        = 1\n', data )
            f.close()
        with open(conf_file_1, 'w') as f:
            f.write(data)

        conf_file_2 = '/etc/systemd/system.conf'
        with open(conf_file_2) as f:
            data = f.read()
            data = re.sub(r'\n#RuntimepipowermeterSec.+\n', '\nRuntimepipowermeterSec=14\n', data )
            f.close()
        with open(conf_file_2, 'w') as f:
            f.write(data)

        with open('/etc/modprobe.d/bcm2835_wdt.conf', 'w') as f:
            data = "alias char-major-10-130 bcm2835_wdt\nalias char-major-10-131 bcm2835_wdt\n"
            f.write(data)

        conf_file_3 = '/etc/modules'
        with open(conf_file_3) as f:
            data = f.read()
            data += "\nbcm2835_wdt\n"
            f.close()
        with open(conf_file_3, 'w') as f:
            f.write(data)
