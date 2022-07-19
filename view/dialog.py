"""
dialog
-----------------------------
popup for adding entries
-----------------------------
"""

import wx


class Dialog (wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.makeContent()
    
    def makeContent(self):
        pass
