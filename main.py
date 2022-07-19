"""
main
-------------------------------------------
info here
--------------------------------------------
"""
import logging

import wx

from control import startup


def getLogger():
    """Sets up my logging system to terminal."""
    log = logging.getLogger("mylogger")
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s - %(funcName)s - %(message)s"
    )
    ch.setFormatter(formatter)
    log.addHandler(ch)
    return log

def main():
    """Main function"""
    log = getLogger()
    if startup.isFirstTime():
        startup.makeFiles
    log.info("Initializing window...")
    app = wx.App()

    app.MainLoop()

if __name__ == "__main__":
     main()
