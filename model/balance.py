"""
balance
--------------------------
balance dataclass
-------------------------
"""


class Balance:
    """A balance. Consists of the name, a inital value and a value.
    """

    def __init__(self, balName, initV, value):
        """Creates a new balance

        Args:
            balName (string): name of balance
            initV (int): init value
            value (int): current value
        """
        self.name = balName
        if self.checkiv(int(initV)):
            self.initValue = initV
        self.value = value

    def checkiv(self, iv):
        """checks if init value is 0 or higher"""
        if iv < 0:
            return False
        return True

    def valueStr(self):
        """For gui display"""
        return str(self.value + self.initValue)
