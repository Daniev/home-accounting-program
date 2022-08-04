"""
result
--------------------------
result dataclass
-------------------------
"""


class Result:
    def __init__(self, catName, value):

        # add a name checker?
        self.name = catName
        self.value = value

    def valueStr(self):
        """For gui display"""
        return str(self.value)
