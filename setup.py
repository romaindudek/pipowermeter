#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from pipowermeter.package.functions import *

def main(argv):
    infos = AppInfos()
    infos.prtHeader()

    if (len(argv) > 0):
        if argv[0] == '-h':
            print (hstr)
            sys.exit()
        elif argv[0] == "install":
            print("installation !")
        elif argv[0] == "uninstall":
            print("uninstallation !")
        elif argv[0] == "trash":
            print("trash !")
        elif argv[0] == "start":
            print("start !")
        elif argv[0] == "stop":
            print("stop !")
        else:
            print (infos.hstr)
            sys.exit()
    else:
            print (infos.hstr)
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])