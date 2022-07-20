"""
main
-------------------------------------------
info here
--------------------------------------------
"""
import wx

from control import startup
from myLogger import getLogger


def main():
    """Main function"""
    log = getLogger()
    if startup.isFirstTime():
        startup.makeFiles()
    log.info("Initializing window...")
    app = wx.App()

    app.MainLoop()

if __name__ == "__main__":
     main()
