# -*- coding: utf-8 -*-

class appProperties:
    VERSION = "0.0.1"
    NAME = "Pi PowerMeter"

    propsArray = [{
                    'name':'deviceName', 
                    'default':'Pi-PowerMeter'
                },{
                    'name':'projectName',
                    'default':'Solar_Panel_1'
                },{
                    'name':'location',
                    'default':'Dieppe, fr'
                },{
                    'name':'apiKey', 
                },{
                    'name':'timeDelay', 
                    'default':180
                },{
                    'name':'portI2C',
                    'default':'45'
                },{
                    'name':'csvSep',
                    'default':','
                },{
                    'name':'record',
                    'default':False
                }]
    
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