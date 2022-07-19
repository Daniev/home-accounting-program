"""
startup
-------------------------------
Creates new files for project
May be ran as script
-----------------------------
"""
import os

import filehandler as fh

from ..main import getLogger


def isFirstTime():
    log = getLogger()
    try:
        data = fh.openFile("entries.json")
        return False
    except:
        log.info("First time -> making files..")
        return True
        

def makeFiles():
    log = getLogger()
    dataDir = "data/"
    isExisting = os.path.exists(dataDir)
    if not isExisting:
        os.makedirs(dataDir)
    fh.openFile("results.json")
    fh.openFile("balances.json")
    fh.openFile("entries.json")

    log.info("files created successfully...")


if __name__ == "__main__":
   makeFiles() 
