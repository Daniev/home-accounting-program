"""
resultpanel
-------------------------------------------------
The result tab displays the current result and 
balance, as well as the transfer between balances
functionality
-------------------------------------------------
"""
import wx

from myLogger import log
from tweakable import BALANCE_ARRAY, BALANCE_CATEGORIES

WIDTHSIZE = 900

class ResultPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=wx.Size(900,WIDTHSIZE))
        self.vSizer = wx.BoxSizer(wx.VERTICAL)
        self.Dialog = B2B(self)
        self.makeResultTable()
        self.makeBalanceTable() 
        b2bButton = wx.Button(self, label="B2B")
        b2bButton.Bind(wx.EVT_BUTTON, self.openB2B)
        self.addToSizer([b2bButton], self.vSizer)
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


    def openB2B(self, event):
        if not self.Dialog:
            self.Dialog = B2B(self)
        self.Dialog.Show()


class B2B(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="B2B", size=wx.Size(600,700))
        self.makeContent()
    
    def makeContent(self):
        label = wx.StaticText(self, label="Balance to subtract from:")
        label2 = wx.StaticText(self, label="Balance to add to:")
        label3 = wx.StaticText(self, label="Value")
        self.inputB1 = wx.ComboBox(self)
        self.inputB2 = wx.ComboBox(self)
        self.inputValue = wx.TextCtrl(self)

        bSizer = wx.BoxSizer(wx.HORIZONTAL)
        b1Sizer = wx.BoxSizer(wx.HORIZONTAL)
        b2Sizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        valueSizer = wx.BoxSizer(wx.HORIZONTAL)
        vSizer = wx.BoxSizer(wx.VERTICAL)

        submitButton = wx.Button(self, label="Submit")
        exitButton = wx.Button(self, label="Exit")

        index = 0
        for category in BALANCE_CATEGORIES():
            self.inputB1.Insert(category, index)
            self.inputB2.Insert(category, index)
            index += 1

        self.inputB1.AutoComplete(BALANCE_ARRAY())
        self.inputB2.AutoComplete(BALANCE_ARRAY())

        self.addToSizer([label, self.inputB1], b1Sizer)
        self.addToSizer([label3, self.inputValue], valueSizer)
        self.addToSizer([label2, self.inputB2], b2Sizer)
        # self.addToSizer([b1Sizer, b2Sizer], bSizer)


        submitButton.Bind(wx.EVT_BUTTON, self.submit)
        exitButton.Bind(wx.EVT_BUTTON, self.exit)

        self.addToSizer([submitButton, exitButton], buttonSizer)

        self.addToSizer([valueSizer, b1Sizer, b2Sizer, buttonSizer], vSizer)
        self.SetSizer(vSizer)


    def addToSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=5)
        return


    def submit(self, event):
        log.info("Submitting...")

    def exit(self, event):
        log.info("Closing dialog..")
        self.Destroy()
