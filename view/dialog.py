"""
dialog
-----------------------------
popup for adding entries
-----------------------------
"""
import wx

from tweakable import RESULT_CATEGORIES


class Dialog (wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, size=wx.Size(600,500), title="add entry")
        self.makeContent()
    
    def makeContent(self):
        vSizer = wx.BoxSizer(wx.VERTICAL)
        mSizer = wx.BoxSizer(wx.HORIZONTAL)
        infMonth = wx.StaticText(self, label="Enter month: ex 'jan'")
        self.inputMonth = wx.TextCtrl(self)
        self.addSizer([infMonth, self.inputMonth], mSizer)

        vaSizer = wx.BoxSizer(wx.HORIZONTAL)
        infValue = wx.StaticText(self, label="Enter value: ex 4000")
        self.inputValue = wx.TextCtrl(self)
        self.addSizer([infValue, self.inputValue], vaSizer)

        poSizer = wx.BoxSizer(wx.HORIZONTAL)
        infPost = wx.StaticText(self, label="Enter post from list")
        self.inputPost = wx.ListCtrl(self)
        # loop to get RESULT_CATEGORIES
        self.addSizer([infPost, self.inputPost], poSizer)
        payBySizer = wx.BoxSizer(wx.HORIZONTAL)
        infPayBy = wx.StaticText(self, label="Which account did the payment")
        self.inputPayBy = wx.Listbook(self)
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
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)


    def submitEntry(self, event):
        pass

    def exitDialog(self, event):
        self.Destroy()
