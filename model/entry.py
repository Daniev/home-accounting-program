"""
entry
---------------------------------------
entry class for storing entries and
validating input data
---------------------------------------
"""
# TODO IMPORT TWEAKABLE
from ..tweakable import RESULT_CATEGORIES


class Entry:
    """Entry: date, value, post, comment"""
    def __init__(self, date, value, post,comment):
        if self.checkValue(date):
            self.date = date

        if self.checkValue(value):
            self.value = value

        if self.checkPost(post):
            self.post = post


        self.comment = comment
        self.isValidInput = True


    def checkPost(self, post):
        """Checks if post is a valid post"""
        for exPost in RESULT_CATEGORIES():
            if exPost == post:
                return True
        return False
            

    def checkValue(self, value):
        try:
            value = int(value)
        except ValueError:
            print("ERROR: value entered is not an int!")
            self.isValidInput = False
            return False
        return True
