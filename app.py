import os
import sys
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from PIL import ImageTk, Image
from ctypes import windll
import aboutPEStart as aboutPE
import infoPEStart as infoPE

# Set most variable for desktop application properties
set_title = "Windows Preinstalled Environment -- Firefly Edition"
set_name_app = "WinPE Start Launcher -- Firefly Edition"
set_background = "files/back/FireflySAM.png"

# Initial w is Tk
w = Tk()
w.title(set_name_app)
w_w, w_h = 600, 400
w_wscr, w_hscr = w.winfo_screenwidth(), w.winfo_screenheight()
x_smW = (w_wscr/2) - (w_w/2)
y_smW = (w_hscr/2) - (w_h/2)
w.geometry(
"%dx%d+%d+%d" %(w_w, w_h, x_smW, y_smW)
)
w.minsize(w_w,w_h)
w.state('zoomed')
# w.maxsize(600,400)
# w.resizable(False, False)
w.overrideredirect(True)
# w.attributes("-alpha", 0.0)
# w.lift()
w.iconbitmap(sys.executable)

# begin menu
menubar = tkinter.Menu(w)

# Exit window and restart from PE mode
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Exit', command = w.destroy)
file.add_command(label ='Shutdown', command = lambda: os.system(f"wpeutil shutdown"))

# Test Menu 1
utils_menu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Tools', menu = utils_menu)
utils_menu.add_command(label ='Command Prompt', command = lambda: os.system(f"start \"Command Prompt in {set_title}\""))
utils_menu.add_command(label ='PowerShell', command = lambda: os.system(f"start powershell -NoExit -command \"$Host.UI.RawUI.WindowTitle = 'Powershell in {set_title}'\""))
utils_menu.add_separator()
utils_menu.add_command(label ='7-Zip File Manager', command = lambda: os.system(f"start 7zfm"))
utils_menu.add_command(label ='Notepad', command = lambda: os.system(f"start notepad"))

# Help and about
help_menubar = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_menubar)
help_menubar.add_command(label = 'Show info', command = infoPE.messageInfoBoxPE)
help_menubar.add_command(label = 'Problem WinPE compatibility', command = infoPE.messagePECompability)
help_menubar.add_command(label = 'About', command = aboutPE.aboutPEStart)
help_menubar.add_command(label = 'About this picture', command = aboutPE.thisIncludedPicture)
help_menubar.add_command(label = 'About WinPE/Windows', command = lambda: os.system(f"start winver"))

# This set Edition
menubar.add_command(label =f"Use for test and release free", state=tkinter.DISABLED, command = None)

w.config(menu=menubar)

# Test background
# Add background image file
bg = PhotoImage(file = set_background)
# Create Canvas
canvas = Canvas( w, width = 600, height = 400)
canvas.pack(fill = "both", expand = True)
# Display image
canvas.create_image( 0, 0, image = bg, anchor = "nw")

def resize_image(e):
   global set_background, image, resized, image2
   # open image to resize it
   image = Image.open(set_background)
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.LANCZOS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor=tkinter.NW, tags="background")
# Bind the function to configure the parent window
w.bind("<Configure>", resize_image)

# Warn to use Windows PE limitaion in duration
tkinter.messagebox.showwarning("Please read this", "In WinPE mode, you can do within 72 hours and can not configured. Make prepare and doing in this time.")
infoPE.messagePECompability()

w.mainloop()