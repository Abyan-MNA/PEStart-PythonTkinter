import os
import sys
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from ctypes import windll

def messageInfoBoxPE():
    tkinter.messagebox.showinfo("Info Windows Preinstalled Environtment",
        """Windows PE is uncomplete rescue kit Windows-based. Some mistake about Windows PE. Windows PE original build with WinAIK or WinADK. Can build with \"builder\" under WinRE.WIM but problem in bluescreen, *DIED.

Useful for beginner Windows PE or technician IT in learning Windows PE App compatible. Command Prompt very basic and uncomfortable for GUI likers.

Please continue quickly in Windows PE Mode.""")

def messagePECompability():
    tkinter.messagebox.showwarning("Problem in Windows PE Compability",
        """Windows PE is not same as Windows OS general like Windows Server 2025, Windows XP, Windows 2000, or Windows 11. More apps is not designed for Windows PE, so you can check application that is running and compatible Windows PE.

You can add or install component with WinADK or WinAIK. Or just use \"builder\" like WinPEBuilder for compability but something happen.""")