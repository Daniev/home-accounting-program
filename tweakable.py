"""
tweakable
---------------------------
Here you will find constants that are likely to be tweaked.
Used throughout the project
---------------------------
"""
from control import startup


def BALANCE_CATEGORIES():
    """Dicts where:
        key = balance name
        value = init value"""
    bc = {}
    bc["student dept"] = 0
    # etc

    return bc


def RESULT_CATEGORIES():
    """List of all result categories"""
    rc = []
    rc.append("income")
    rc.append("loan payout")
    return rc


if __name__ == "__main__":
    # run tweakable to reset the datafiles
    startup.makeFiles()


 
