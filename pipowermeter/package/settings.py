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
        self.locals = self.local_dir(".locals")
        self.locals = self.get_or_set_local("locals", self.locals, hide=True)['varSet']
        self.baseDir = self.get_or_set_local("baseDir", self.baseDir, hide=True)['varSet']
        self.datas = self.local_dir("datas")
        self.deviceName = self.get_or_set_local("deviceName", "pipowermeter1", hide=True)['varSet']
        self.location = self.get_or_set_local("location", "Dieppe", hide=True)['varSet']
    
    def get_or_set_local(self, localSetting, settingValue, hide=False):
        """
        Get or sets a local setting,
        creates it if it is not present.
        """
        if hide:
            localFilePath = self.locals + '.' + localSetting
        else:
            localFilePath = self.locals + localSetting
        return pickle_gt_or_set(localFilePath, settingValue)

    def overwrite_local(self, localSetting, settingValue, hide=False):
        """
        Overwrite a local setting
        """
        if hide:
            localFilePath = self.locals + '.' + localSetting
        else:
            localFilePath = self.locals + localSetting
        return pickle_wr(localFilePath, settingValue)

    def local_dir(self, dirName):
        """

        """
        localdirname = self.baseDir + os.path.sep + dirName + os.path.sep
        print(dirName + " : " + localdirname)
        if not os.path.exists(localdirname):
            os.makedirs(localdirname)
        return localdirname
    
# Functions ----------------------------------------------------------------


    

