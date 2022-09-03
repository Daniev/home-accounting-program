"""
entry
---------------------------------------
entry class for storing entries and
validating input data
---------------------------------------
"""
from myLogger import log
# TODO IMPORT TWEAKABLE
from tweakable import BALANCE_CATEGORIES, RESULT_CATEGORIES


class Entry:
    """Entry: month, value, post, payBy, comment"""

    def __init__(self, month, value, post, payBy, comment):
        """Creates an entry

        Args:
            month (string): month ex jan
            value (int): value of the entry
            post (string): the result category the entry should affect
            payBy (string): account name who paid the value
            comment (string): any comment of the entry...
        """
        self.isValidInput = True
        if self.checkMonth(month):
            self.month = month

        if self.checkValue(value):
            self.value = value

        if self.checkPost(post):
            self.post = post

        if self.checkPayBy(payBy):
            self.payBy = payBy

        self.comment = comment

    def checkPost(self, post):
        """Checks if post is a valid post"""
        for exPost in RESULT_CATEGORIES:
            if exPost == post:
                return True
        self.isValidInput = False
        log.error("Entered post is invalid!")
        return False

    def checkValue(self, value):
        """Checks the validity of the value

        Args:
            value (int): hopefully int

        Returns:
            bool: True if valid.
        """
        try:
            value = int(value)
        except ValueError:
            log.error("value entered is not an int!")
            self.isValidInput = False
            return False
        return True

    def checkMonth(self, month):
        """Checks if month is entered successfully

        Args:
            month (string): month selected in entry

        Returns:
            bool: true if valid.
        """
        allMonths = ["jan", "feb", "mar", "apr", "may",
                     "jun", "jul", "aug", "sep", "okt",
                     "nov", "des"]
        for correct in allMonths:
            if month == correct:
                return True
        log.error("Month is not a valid output...")
        self.isValidInput = False
        return False

    def checkPayBy(self, payBy):
        """Checks validity of pay by value

        Args:
            payBy (string): balance account

        Returns:
            bool: true if valid.
        """
        for bal in BALANCE_CATEGORIES:
            if payBy == bal:
                return True
        self.isValidInput = False
        log.error("PayBy value is invalid...")
        return False

    def valueStr(self):
        return str(self.value)
