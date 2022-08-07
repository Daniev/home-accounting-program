"""
dialog
--------------------------------------
popup for adding entries
--------------------------------------
"""

import wx

from control import date, interface
from myLogger import log
from tweakable import BANKS, RESULT_CATEGORIES


class Dialog (wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, size=wx.Size(600, 500), title="add entry")
        self.makeContent()

    def makeContent(self):
        vSizer = wx.BoxSizer(wx.VERTICAL)
        mSizer = wx.BoxSizer(wx.HORIZONTAL)
        infMonth = wx.StaticText(self, label="Enter month: ex 'jan'")
        self.inputMonth = wx.TextCtrl(self)
        currentMonth = date.getCurrentMonth()
        self.inputMonth.SetValue(date.getMonthText(currentMonth))
        self.addSizer([infMonth, self.inputMonth], mSizer)

        vaSizer = wx.BoxSizer(wx.HORIZONTAL)
        infValue = wx.StaticText(self, label="Enter value: ex 4000")
        self.inputValue = wx.TextCtrl(self)
        self.addSizer([infValue, self.inputValue], vaSizer)

        poSizer = wx.BoxSizer(wx.HORIZONTAL)
        infPost = wx.StaticText(self, label="Enter post from list")
        self.inputPost = wx.ComboBox(self)
        # loop to get RESULT_CATEGORIES
        i = 0
        for category in RESULT_CATEGORIES:
            self.inputPost.Insert(category, i)
            i += 1

        self.inputPost.AutoComplete(RESULT_CATEGORIES)
        self.addSizer([infPost, self.inputPost], poSizer)

        payBySizer = wx.BoxSizer(wx.HORIZONTAL)
        infPayBy = wx.StaticText(self, label="Which account did the payment")
        self.inputPayBy = wx.ComboBox(self)
        i = 0
        for category in BANKS:
            self.inputPayBy.Insert(category, i)
            i += 1
        self.inputPayBy.AutoComplete(BANKS)
        self.addSizer([infPayBy, self.inputPayBy], payBySizer)

        cSizer = wx.BoxSizer(wx.HORIZONTAL)
        infComment = wx.StaticText(self, label="comment:")
        self.inputComment = wx.TextCtrl(self)
        self.addSizer([infComment, self.inputComment], cSizer)

        self.addSizer([mSizer, vaSizer, poSizer, payBySizer, cSizer], vSizer)

        submitButton = wx.Button(self, label="submit")
        exitButton = wx.Button(self, label="exit")

        submitButton.Bind(wx.EVT_BUTTON, self.submitEntry)
        exitButton.Bind(wx.EVT_BUTTON, self.exitDialog)

        self.addSizer([submitButton, exitButton], vSizer)
        self.SetSizer(vSizer)
        return

    def addSizer(self, list, sizer):
        """Internal function. Used to add elements to sizer."""
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return

    def resetInputs(self):
        """Resets all textctrls input. Used to clear user input"""
        self.inputMonth.SetValue("")
        self.inputValue.SetValue("")
        self.inputPost.SetValue("")
        self.inputPayBy.SetValue("")
        self.inputComment.SetValue("")

    def submitEntry(self, event):
        log.info("Submitting entry...")

        month = self.inputMonth.GetValue()
        value = self.inputValue.GetValue()
        post = self.inputPost.GetValue()
        payBy = self.inputPayBy.GetValue()
        comment = self.inputComment.GetValue()

        interface.addNewEntry(month, value, post, payBy, comment)
        self.resetInputs()

    def exitDialog(self, event):
        self.resetInputs()
        self.Hide()
