"""
interface
-----------------------------------
provides an interface from view to rest and back
-----------------------------------
"""
from control import dictmapper as dm
from control import filehandler as fh
from myLogger import log


def getResult():
    """returns list of result instances"""
    results =fh.openFile("results.json")
    cResults = []
    for result in results:
        cResults.append(dm.ResMapper.dictToClass(result, results[result]))

    log.info("fetched stored results..")
    return cResults
    
    

def getBalance():
    """returns list of balance instances"""
    balances = fh.openFile("balances.json")
     
    cBalances = []
    for balance in balances:
        cBalances.append(dm.BalMapper.dictToClass(balance, balances[balance]))
    log.info("Fetched stored balances..")
    return cBalances


def writeResult(results):
    data = []
    for result in results:
        data.append(dm.ResMapper.classToDict(result)) 
    fh.writeFile("results.json", data)
    log.info("results are written..")
    return


def writeBalance(balances):
    data = {}
    for balance in balances:
        temp = dm.BalMapper.classToDict(balance)
        for t in temp: # move the key t to data {t: {iv v}} becomes t: {iv v}
            data[t] = temp[t]

    fh.writeFile("balances.json", data)
    log.info("balances are written..")


def getEntries():
    entries=fh.openFile("entries.json")
    cEntries= []
    for entry in entries:
        cEntries.append(dm.EntryMapper.dictToClass(entry))

    log.info("fetched stored entries..")
    return cEntries
    
    
def writeEntries(entries):
    data = []
    for entry in entries:
        data.append(dm.EntryMapper.classToDict(entry))

    fh.writeFile("entries.json", data)
    log.info("entries are written..")
