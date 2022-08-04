"""
mainpanel
---------------------------
displays existing entries and the button to
add a new entry
---------------------------
"""

import wx

from view import dialog

WIDTHSIZE = 900


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=wx.Size(900, WIDTHSIZE))
        self.dialog = dialog.Dialog(self)
        self.makeContent()

    def makeContent(self):
        # show entries
        vSizer = wx.BoxSizer(wx.VERTICAL)
        columnWidth = int(WIDTHSIZE // 5 - 2)
        self.displayEntries = wx.ListView(self)
        self.displayEntries.InsertColumn(0, "month", width=columnWidth)
        self.displayEntries.InsertColumn(1, "value", width=columnWidth)
        self.displayEntries.InsertColumn(2, "post", width=columnWidth)
        self.displayEntries.InsertColumn(3, "payed_by", width=columnWidth)
        self.displayEntries.InsertColumn(4, "comment", width=columnWidth)

        # make entries button
        addButton = wx.Button(self, label="add entry")
        addButton.Bind(wx.EVT_BUTTON, self.showDialog)

        refreshButton = wx.Button(self, label="refresh entries")
        refreshButton.Bind(wx.EVT_BUTTON, self.refreshEntries)
        self.addSizer([self.displayEntries, addButton, refreshButton], vSizer)

        self.SetSizer(vSizer)

    def showDialog(self, event):
        if not self.dialog:
            self.dialog = dialog.Dialog(self)
        self.dialog.Show()

    def addSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return

    def refreshEntries(self, event):
        # get entries

        # display them..
        pass
