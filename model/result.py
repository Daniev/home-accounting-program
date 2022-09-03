"""
result
--------------------------
result dataclass
-------------------------
"""


class Result:
    def __init__(self, catName, value):
        """Create a new result category

        Args:
            catName (string): name
            value (int): start value, likely 0
        """

        # add a name checker?
        self.isValid = True
        self.name = catName
        if self.checkValue(value):
            self.value = int(value)

    def valueStr(self):
        """For gui display"""
        return str(self.value)

    def checkValue(self, value):
        try:
            int(value)
            return True
        except ValueError:
            print("Invalid result value!")
            self.isValid = False
            return False
