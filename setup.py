#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

from pipowermeter.package.functions import *
from pipowermeter.package.output import OutputMeasure


def main(argv):

    output = OutputMeasure()
    output.print_measure()
    print(output.line_measure())

    init = AppInit()
    init.prt_header()

    ser = ServiceManage()
    print("Pi Powermeter statuses : Loaded = %s | Active = %s" % (ser.isLoaded, ser.isActive))

    if (len(argv) == 1):
        if argv[0] == '-h':
            print (init.hstr)
            sys.exit()
        elif argv[0] == "install":
            inst = Installation()
            inst.install()

        elif argv[0] == "uninstall":
            inst = Installation()
            inst.uninstall()

        elif argv[0] == "trash":
            inst = Installation()
            inst.trash()

        elif argv[0] == "start":
            inst = Exec()
            inst.m_start()
        elif argv[0] == "stop":
            inst = Exec()
            inst.m_stop()
        else:
            print (init.hstr)
            sys.exit()
    else:
            print (init.hstr)
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])