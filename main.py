"""
main
-------------------------------------------
info here
--------------------------------------------
"""
import wx

from control import startup
from myLogger import log
from view import window


def main():
    """Main function"""
    print("---------------Starting up ---------------")
    if startup.isFirstTime():
        startup.makeFiles()
    else:
        log.info("Skipping startup..")
    log.info("Initializing window...")
    app = wx.App()
    window.Window()

    app.MainLoop()


if __name__ == "__main__":
    main()
