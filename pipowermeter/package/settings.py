#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pickle

from .functions import * 
from .properties import appProperties

class MySettings:
    """
    Get or set local settings
    """
    def __init__(self):
        self.baseDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        self.locals = self.local_dir(".locals")
        self.locals = self.get_or_set_local("locals", self.locals)['varSet']
        self.baseDir = self.get_or_set_local("baseDir", self.baseDir)['varSet']
        self.datas = self.local_dir("datas")
        self.propertiesArray = appProperties.propsArray
        self.refresh()

    def refresh(self):
        for prop in self.propertiesArray:
            propName = prop['name']
            try:
                propVal = prop['default'].replace(" ", "_")
            except:
                propVal = None
            setattr(self, prop['name'], self.get_or_set_local(propName, propVal)['varSet'])

    
    def get_or_set_local(self, localSetting, settingValue=None):
        """
        Get or sets a local setting,
        creates it if it is not present.
        """
        localFilePath = self.get_local_file_path(localSetting)
        return pickle_get_or_set(localFilePath, settingValue)

    def set_local(self, localSetting, settingValue):
        """
        Sets a local setting,
        creates it if it is not present.
        """
        localFilePath = self.get_local_file_path(localSetting)
        return pickle_wr(localFilePath, settingValue)

    def get_local_file_path(self, localSetting):
        return self.locals + '.' + localSetting

    def local_dir(self, dirName):
        """
        Get a local dir from its dirName or create if not exists
        """
        localdirname = self.baseDir + os.path.sep + dirName + os.path.sep
        if not os.path.exists(localdirname):
            os.makedirs(localdirname)
        return localdirname
    
# Functions ----------------------------------------------------------------



    

