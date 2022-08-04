"""
tweakable
---------------------------
Here you will find constants that are likely to be tweaked.
Used throughout the project
---------------------------
"""
from control import startup

"""
-----------------------------------------------
Balance and result handling
-----------------------------------------
"""
# for the payBy choice
BANKS = ["brukskonto", "regninger", "buffer", "langsiktig_sparing"]

# List of incomes used in balance handling
LIST_OF_INCOMES = ["annen_inntekt", "lønn", "lånutbetaling"]

# dictionary of balance names and init values
BALANCE_CATEGORIES = {"brukskonto": 0, "regninger": 0, "buffer": 0,
                      "langsiktig_sparing": 0, "bsu": 0, "mastercard": 0,

                      "studentlån": 0, "studentlån_d": 0,
                      "studentlån_m": 0,

                      "interiør": 0, "eiendom": 0, "skyldig_skatt": 0}

# only balance names in a list
BALANCE_ARRAY = []
for i in BALANCE_CATEGORIES:
    BALANCE_ARRAY.append(i)

# list of all result categories
RESULT_CATEGORIES = ["annen_inntekt", "lønn", "lånutbetaling",

                     "skatt", "lån_nedbetaling", "bil", "bilforsikring",
                     "drivstoff", "annen_forsikring", "husleie", "strøm",

                     "mat", "underholdning", "interiør", "hobby"]


"""
---------------------------------------------------------------
Run this script to reset the files of the project...
--------------------------------------------------------------
"""
if __name__ == "__main__":
    # run tweakable to reset the datafiles
    startup.makeFiles()
