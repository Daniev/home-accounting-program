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
BANKS = ["brukskonto", "regninger", "buffer", "langsiktig_sparing",
         "mastercard"]

# List of incomes used in balance handling
LIST_OF_INCOMES = ["annen_inntekt", "lønn"]

# dictionary of balance names and init values
BALANCE_CATEGORIES = {"brukskonto": 5442, "regninger": 9000, "buffer": 45000,
                      "langsiktig_sparing": 356000, "bsu": 127000,
                      "mastercard": 0,

                      "studentlån": 600000, "studentlån_d": 300000,
                      "studentlån_m": 300000,

                      "interiør": 0, "eiendom": 0, "skyldig_skatt": 0}

# only balance names in a list
BALANCE_ARRAY = []
for i in BALANCE_CATEGORIES:
    BALANCE_ARRAY.append(i)

# list of all result categories
RESULT_CATEGORIES = ["annen_inntekt", "lønn",

                     "skatt", "bil", "bilforsikring",
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
