#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from .functions import pickle_gt_or_set, pickle_wr

class MySettings:
    """
    Get or set local settings
    """
    def __init__(self):
        self.baseDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        print("basedir : " + self.baseDir)
        self.locals = self.get_local_dirname()
        self.deviceName = self.get_or_set_local("deviceName", "pipowermeter1", hide=True)
        self.location = self.get_or_set_local("location", "Dieppe", hide=True)
    
    def get_or_set_local(self, localSetting, settingValue, hide=False):
        """
        Get or sets a local setting,
        creates it if it is not present.
        """
        if hide:
            local_filepath = self.locals + '.' + localSetting
        else:
            local_filepath = self.locals + localSetting
        return pickle_gt_or_set(local_filepath, settingValue)



    def get_local_dirname(self):
        localdirname = self.baseDir + os.path.sep + ".locals" + os.path.sep
        print("localdirname : " + localdirname)
        if not os.path.exists(localdirname):
            os.makedirs(localdirname)
        return localdirname
    
# Functions ----------------------------------------------------------------


    

