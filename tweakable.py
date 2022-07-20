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
    # accounts
    bc["user_account"] = 0
    bc["bills_account"] = 0
    bc["short_savings"] = 0
    bc["long_savings"] = 0
    bc["bsu"] = 0
    bc["credit_account"] = 0 # master card

    # dept
    bc["student_dept_m"] = 0
    bc["student_dept_d"] = 0
    bc["student_dept"] = 0

    # others
    bc["interior"] = 0
    bc["property"] = 0 # houses and such
    bc["owed_taxes"] = 0

    return bc


def RESULT_CATEGORIES():
    """List of all result categories"""
    rc = []
    rc.append("other_income") # gifts, interests, investmentincome etc
    rc.append("wages") # work income
    rc.append("loan_payout") #income from loan

    rc.append("taxes")
    rc.append("loan_payoff") #payoff of loan
    rc.append("car")
    rc.append("car_insurance")
    rc.append("fuel")
    rc.append("other_insurance")
    rc.append("house_rent")
    rc.append("electricity")

    rc.append("food")
    rc.append("entertainment") # streaming services etc
    rc.append("interior") # things needed in a household including tools
    rc.append("hobby") # music equpment, technology, nitting etc

    return rc


if __name__ == "__main__":
    # run tweakable to reset the datafiles
    startup.makeFiles()


 
