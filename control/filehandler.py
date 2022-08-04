#! usr/bin/python

"""
filehandler
----------------------------------------
Functions which reads and writes to the file
specified..
-----------------------------------------"""
import json


def openFile(filename):
    """Opens Jsonfile and returns all the data"""
    with open("data/"+filename, mode="r", encoding="utf8") as jsonFile:
        data = json.load(jsonFile)
    return data


def writeFile(filename, data):
    """Dumps whole data to jsonfile and saves it."""
    with open("data/"+filename, mode="w", encoding="utf8") as jsonFile:
        json.dump(data, jsonFile, indent=4)
