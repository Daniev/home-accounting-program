"""
window
----------------------
main window of gui
---------------------
"""


import wx

from view import mainpanel


class Window(wx.Frame):
    def __init__(self):
        super().__init__() # add size and title
        self.makeContent()


    def makeContent(self):
        vSizer = wx.BoxSizer(wx.VERTICAL)
        notebook = wx.Notebook(self, wx.RIGHT)
        defaultPanel = mainpanel.MainPanel(notebook)
        notebook.AddPage(defaultPanel, "entries")
        self.addSizer([notebook], vSizer)

        self.SetSizer(vSizer)
        self.Show()



    def addSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return
