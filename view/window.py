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
        notebook = wx.Notebook(self, wx.RIGHT, size=wx.Size(900, 700))
        defaultPanel = mainpanel.MainPanel(notebook)
        resultPanel = resultpanel.ResultPanel(notebook)
        notebook.AddPage(defaultPanel, "Entries")
        notebook.AddPage(resultPanel, "Result")
        self.addSizer([notebook], vSizer)

        self.SetSizer(vSizer)
        self.Show()

    def addSizer(self, list, sizer):
        for i in list:
            sizer.Add(i, flag=wx.EXPAND | wx.ALL, border=8)
        return
