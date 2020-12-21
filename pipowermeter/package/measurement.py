#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import time
from .ina219 import INA219

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.2


def read():
    ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS, log_level=logging.INFO, busnum=0x45)
    ina.configure(ina.RANGE_32V, ina.GAIN_AUTO)

    print("Bus Voltage    : %.3f V" % ina.voltage())
    print("Bus Current    : %.3f mA" % ina.current())
    print("Supply Voltage : %.3f V" % ina.supply_voltage())
    print("Shunt voltage  : %.3f mV" % ina.shunt_voltage())
    print("Power          : %.3f mW" % ina.power())

class PowerMeasure:

    def __init__(self):
        self.pwr_measure()
        if self.error != False:
            self.voltage = None
            self.current = None
            self.power = None

    def pwr_measure(self):
        try:
            ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
            ina.configure(ina.RANGE_16V, ina.GAIN_AUTO)
            self.voltage = round(ina.voltage(),1)
            self.current = round(ina.current(), 1)
            self.power = round(ina.power()/100, 1)
            self.error = False 

        except Exception as e:
            self.error = str(e)

if __name__ == "__main__":
    while True :
        read()
        time.sleep(10)

