from Tkinter import Tk
from tkFileDialog import askopenfilename
import tkMessageBox

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

tkMessageBox.showinfo(title="Greetings", message="Hello World!")