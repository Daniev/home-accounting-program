"""
resultpanel
-------------------------------------------------
The result tab displays the current result and
balance, as well as the transfer between balances
functionality
-------------------------------------------------
"""
import wx

from control import interface
from myLogger import log
from tweakable import BALANCE_ARRAY, BALANCE_CATEGORIES, RESULT_CATEGORIES

WIDTHSIZE = 900


class ResultPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=wx.Size(900, WIDTHSIZE))
        self.vSizer = wx.BoxSizer(wx.VERTICAL)
        self.makeResultTable()
        self.makeBalanceTable()
        self.SetSizer(self.vSizer)

    def makeResultTable(self):
        label = wx.StaticText(self, label="Current Result")
        self.displayResult = wx.ListView(self)
        columWidth = int(WIDTHSIZE // 2 - 3)
        self.displayResult.InsertColumn(0, "Category", width=columWidth)
        # TODO: change value to spesific month name
        self.displayResult.InsertColumn(1, "Value", width=columWidth)

        self.fillResults()
        self.addToSizer([label, self.displayResult], self.vSizer)

    def fillResults(self):
        index = 0
        allResults = interface.FileHandler.getResult()
        # will be a list of results in class mode...
        for cat in allResults:
            self.displayResult.InsertItem(index, cat.name)
            self.displayResult.SetItem(index, 1, str(cat.value))

    def fillBalance(self):
        index = 0
        allBalances = interface.FileHandler.getBalance()
        for cat in allBalances:
            self.displayBalance.InsertItem(index, cat.name)
            self.displayBalance.SetItem(index, 1, cat.valueStr())

    def makeBalanceTable(self):
        label2 = wx.StaticText(self, label="Current Balance")
        columnWidth = int(WIDTHSIZE // 2 - 3)
        self.displayBalance = wx.ListView(self)
        self.displayBalance.InsertColumn(0, "Category", width=columnWidth)
        self.displayBalance.InsertColumn(1, "Value", width=columnWidth)

        self.fillBalance()
        self.addToSizer([label2, self.displayBalance], self.vSizer)

    def addToSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return
