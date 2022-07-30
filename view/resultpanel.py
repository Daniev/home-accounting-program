"""
resultpanel
-------------------------------------------------
The result tab displays the current result and 
balance, as well as the transfer between balances
functionality
-------------------------------------------------
"""

import wx

WIDTHSIZE = 900

class ResultPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=wx.Size(900,WIDTHSIZE))
        self.vSizer = wx.BoxSizer(wx.VERTICAL)
        self.makeResultTable()
        self.makeBalanceTable() 
        self.SetSizer(self.vSizer)


    def makeResultTable(self): 
        label = wx.StaticText(self, label="Result")
        self.displayResult = wx.ListView(self)
        columWidth = int(WIDTHSIZE // 2 - 3)
        self.displayResult.InsertColumn(0, "Category",width=columWidth)
        self.displayResult.InsertColumn(1, "Value", width=columWidth) # change to monthname
        self.addToSizer([label, self.displayResult], self.vSizer)
 

    def makeBalanceTable(self):
        label2 = wx.StaticText(self, label="Current Balance")
        columnWidth =int (WIDTHSIZE // 2 - 3)
        self.displayBalance = wx.ListView(self)
        self.displayBalance.InsertColumn(0, "Category", width=columnWidth)
        self.displayBalance.InsertColumn(1, "Value", width=columnWidth)
        self.addToSizer([label2, self.displayBalance], self.vSizer)

    def addToSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return


    
