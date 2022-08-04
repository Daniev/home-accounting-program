"""
interface
-----------------------------------
provides an interface from view to rest and back
-----------------------------------
"""
from control import dictmapper as dm
from control import filehandler as fh
from model import balance, entry, result
from myLogger import log
from tweakable import LIST_OF_INCOMES


class FileHandler:
    """Functions for retrieving existing data
    and store new data"""
    def __init__(self) -> None:
        pass
    @staticmethod
    def getResult():
        """returns list of result instances"""
        results = fh.openFile("results.json")
        cResults = []
        for res in results:
            cResults.append(dm.ResMapper.dictToClass(res, results[res]))

        log.info("fetched stored results..")
        return cResults

    @staticmethod
    def getBalance():
        """returns list of balance instances"""
        balances = fh.openFile("balances.json")

        cBalances = []  
        for balance in balances:
            cBalances.append(dm.BalMapper.dictToClass(balance, balances[balance]))
        log.info("Fetched stored balances..")
        return cBalances

    @staticmethod
    def writeResult(results):
        data = []
        for res in results:
            data.append(dm.ResMapper.classToDict(res))
        fh.writeFile("results.json", data)
        log.info("results are written..")
        return

    @staticmethod
    def writeBalance(balances):
        data = {}
        for bal in balances:
            temp = dm.BalMapper.classToDict(bal)
            for t in temp:  # move the key t to data {t: {iv v}} becomes t: {iv v}
                data[t] = temp[t]

        fh.writeFile("balances.json", data)
        log.info("balances are written..")

    @staticmethod
    def getEntries():
        entries = fh.openFile("entries.json")
        cEntries = []
        for ent in entries:
            cEntries.append(dm.EntryMapper.dictToClass(ent))

        log.info("fetched stored entries..")
        return cEntries

    @staticmethod
    def writeEntries(entries):
        data = []
        for ent in entries:
            data.append(dm.EntryMapper.classToDict(ent))

        fh.writeFile("entries.json", data)
        log.info("entries are written..")


class EntryHandler:
    def __init__(self) -> None:
        pass

    @staticmethod
    def addNewEntry(month, value, post, payBy, comment):
        newEntry = entry.Entry(month, value, post, payBy, comment)
        entries = FileHandler.getEntries()
        entries.append(newEntry)
        FileHandler.writeEntries(entries)
        log.info("Success!")


def updateBalance(entry):
    oldBalance = FileHandler.getBalance()

    for income in LIST_OF_INCOMES:
        if entry.post == income:
            oldBalance[entry.payBy] += entry.value
        else:
            # subtract entry value from selected bank account
            oldBalance[entry.payBy] -= entry.value
