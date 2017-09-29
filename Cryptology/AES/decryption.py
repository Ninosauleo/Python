import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import sys
from Tkinter import *
import Tkinter, tkFileDialog

from tkFileDialog import askopenfilename
import ast
import os
import tkMessageBox
from collections import Counter

fileDir = os.path.dirname(os.path.realpath('__file__'))


def pop_window(title, message):
    tkMessageBox.showinfo(title, message)

def select_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename


def main():
    pop_window("SELECT KEY", "KEY.TXT from your computer")
    filename = select_file()
    print(filename)
    file = open(filename, 'r')
    my_key = file.readline()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(my_key, AES.MODE_CFB, iv)
    file.close()

    pop_window("SELECT CIPHER TEXT", "ciphertext.TXT from your computer")
    filename = select_file()
    file = open(filename, 'r')
    msg = file.readline()
    decrypted = cipher.decrypt(msg)
    file.close()
    print decrypted


main()
