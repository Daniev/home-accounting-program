"""
startup
-------------------------------
Creates new files for project
May be ran as script
-----------------------------
"""
import os

from myLogger import getLogger
from tweakable import BALANCE_CATEGORIES, RESULT_CATEGORIES

from . import filehandler as fh


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

    fh.writeFile("entries.json", [])

    log.info("files created successfully...")

    fh.writeFile("balances.json", resetBalanceData())
    log.info("added balance values..")

    fh.writeFile("results.json", resetResultData())
    log.info("added resultvalues..")


def resetResultData():
    """Converts the list to a dict where list
    becomes keys with value 0"""
    resData = {}
    for resCat in RESULT_CATEGORIES:
        resData[resCat] = 0
    return resData


def resetBalanceData():
    balData = {}
    balCats = BALANCE_CATEGORIES
    for balCat in balCats:
        balData[balCat] = {"init_value": balCats[balCat], "value": 0}
    return balData


if __name__ == "__main__":
    makeFiles()
