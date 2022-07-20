"""
main
-------------------------------------------
info here
--------------------------------------------
"""
import wx

from control import startup
from myLogger import log


def main():
    """Main function"""
    if startup.isFirstTime():
        startup.makeFiles()
    else:
        log.info("Skipping startup..")
    log.info("Initializing window...")
    app = wx.App()

    app.MainLoop()

if __name__ == "__main__":
     main()
