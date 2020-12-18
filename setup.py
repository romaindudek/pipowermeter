#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from pipowermeter.package.functions import *

def main(argv):
    init = AppInit()
    init.prtHeader()

    if (len(argv) == 1):
        if argv[0] == '-h':
            print (init.hstr)
            sys.exit()
        elif argv[0] == "install":
            inst = Installation()
            inst.install()

        elif argv[0] == "uninstall":
            print("uninstallation !")
        elif argv[0] == "trash":
            print("trash !")
        elif argv[0] == "start":
            print("start !")
        elif argv[0] == "stop":
            print("stop !")
        else:
            print (init.hstr)
            sys.exit()
    else:
            print (init.hstr)
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])