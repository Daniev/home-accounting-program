"""
window
--------------------------------------------------------------
main window/ frame of gui. Consists of multiple
notebooks/tabs with different content, all of which are loaded
at stratup.
---------------------------------------------------------------
"""


import wx

from view import mainpanel, resultpanel


class Window(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, size=wx.Size(905, 705))
        self.makeContent()

    def makeContent(self):
        vSizer = wx.BoxSizer(wx.VERTICAL)
        self.notebook = wx.Notebook(self, wx.RIGHT, size=wx.Size(900, 700))
        self.defaultPanel = mainpanel.MainPanel(self.notebook)
        self.resultPanel = resultpanel.ResultPanel(self.notebook)
        self.notebook.AddPage(self.defaultPanel, "Entries")
        self.notebook.AddPage(self.resultPanel, "Result")
        self.addSizer([self.notebook], vSizer)
        self.notebook.Bind(wx.EVT_BUTTON, self.sendUp)
        self.Bind(wx.EVT_BUTTON, self.refreshAll)

        self.SetSizer(vSizer)
        self.Show()

    def addSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return

    def refreshAll(self, event):
        self.defaultPanel.displayEntries.DeleteAllItems()
        self.defaultPanel.fillEntries()

        self.resultPanel.displayResult.DeleteAllItems()
        self.resultPanel.fillResults()
        self.resultPanel.displayBalance.DeleteAllItems()
        self.resultPanel.fillBalance()

    def sendUp(self, event):
        event.Skip()
