"""
main
-------------------------------------------
info here
--------------------------------------------
"""
import logging

import wx

from control import filehandler, startup


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
    app = wx.App()

    log.info("Initializing window...")
    app.MainLoop()

    entry_manager.update_entry_size_json()


if __name__ == "__main__":
     main()
