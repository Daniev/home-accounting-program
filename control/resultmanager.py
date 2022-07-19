#! usr/bin/python

# resultmanager.py
import time

from filehandler import openFile, writeFile


class ResultManager:
    def __init__(self, log) -> None:
        self.log = log

        self.resultsMonth = {}  # all results of current month
        self.allResults = {}

    def getCurrentMonth(self):
        """Returns current month in lowercase"""
        timeNow = time.asctime().lower()
        timeNow = timeNow.split(" ")
        return timeNow[1]  # second word is month

    def mapMonthAndNumber(self, month):
        """Maps a month value to a numerical value, to locate correct column in json

        returns:
            columnNr (int)"""
        months = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "okt": 10,
            "nov": 11,
            "des": 12,
        }
        return months[month - 1]

    def importResults(self):
        """Imports results for current month. Maps all to self.allResults"""
        self.allResults = openFile("files/results.json")
        month = self.getCurrentMonth()
        self.resultsMonth = self.allResults[self.mapMonthAndNumber(month)]

    def saveResults(self):
        """Saves results to results.json"""
        writeFile("files/results.json", self.allResults)

    def resultsCurrentMonth(self):
        """Returns the result of this current month"""
        month = self.getCurrentMonth()
        resCurMonth = {}
        for post in self.allResults:
            resCurMonth[post] = self.allResults[post][self.mapMonthAndNumber(
                month)]
        return resCurMonth

    def resultsForMonth(self, month):
        """Returns result of month provided."""
        return self.allResults[self.mapMonthAndNumber(month)]

    def updateResultAt(self, post, value):
        """Updates result at post by adding value

        Args:
            post (str): postname
            value (int): value to add
        """
        month = self.getCurrentMonth()
        postArray = self.allResults[post]
        postArray[self.mapMonthAndNumber(month)] += value
        self.log.info(f"Updated value at {post} in month {month}")

    def createBlankResults(self, rcategories):
        """Creates init values (0 for all 12 months) for all result categories.
        and saves them in results.json

        Args:
            rcategories (list): result categories.
        """
        data = {}

        for cat in rcategories:
            # Fill every category with values of 0 for every month
            data[cat] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        writeFile("files/results.json", data)
