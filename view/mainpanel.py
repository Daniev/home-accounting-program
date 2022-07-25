"""
mainpanel
---------------------------
displays existing entries and the button to
add a new entry
---------------------------
"""

import wx

# from view import dialog


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.makeContent()

    def makeContent(self):
        # show entries
        vSizer =wx.BoxSizer(wx.VERTICAL)
        self.displayEntries = wx.ListView(self)
        self.displayEntries.InsertColumn(0, "month")
        self.displayEntries.InsertColumn(1, "value")
        self.displayEntries.InsertColumn(2, "post")
        self.displayEntries.InsertColumn(3, "payed_by")
        self.displayEntries.InsertColumn(4, "comment")

        # make entries button
        addButton = wx.Button(self)
        addButton.Bind(wx.EVT_BUTTON, self.showDialog)
        self.addSizer([self.displayEntries, addButton], vSizer)



    def showDialog(self, event):
        pass

    
    def addSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return 
