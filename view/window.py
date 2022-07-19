"""
window
----------------------
main window of gui
---------------------
"""

import wx


class Window(wx.Frame):
    def __init__(self):
        super().__init__() # add size and title

    # notebooks -> tabs can add panels to it..
    # add panels with notebook as parent
    # wx.Notebooks(parent, wx.RIGHT)
