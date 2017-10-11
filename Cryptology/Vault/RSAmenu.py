from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
from collections import Counter
from Tkinter import Tk
from tkFileDialog import askopenfilename
import ast
import os
import tkMessageBox
from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox
from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
from collections import Counter
from Tkinter import Tk
from tkFileDialog import askopenfilename
import ast
import os
import tkMessageBox
from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox


fileDir = os.path.dirname(os.path.realpath('__file__'))

def ask_user(prompt, command):
    root = Tkinter.Tk()
    var = tkSimpleDialog.askstring(str(prompt), str(command))
    #print var
    return var

def read_file_line(file_name):
    filename = os.path.join(fileDir, str(file_name))
    with open(filename, 'r') as f:
        read_data = f.readline()
        return read_data


def read_key_file(key_name):
    filename = os.path.join(fileDir, str(key_name))
    with open(filename, 'r') as f:
        read_data = f.readline()
        return read_data


def read_file_all(file_name):
    filename = os.path.join(fileDir, str(file_name))
    with open(filename, 'r') as f:
        read_data = f.readlines()
        return read_data


def pop_window(title, message):
    tkMessageBox.showinfo(title, message)


def select_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename


def hash_sha512(message):
    # SHA512 HASHING OF THE INPUT FILE
    h = SHA512.new()
    h.update(str(message))
    # digest() Return the binary (non-printable) digest of the message that has been hashed so far.
    # hexdigest() Return the printable digest of the message that has been hashed so far.
    signature = h.hexdigest()
    return signature


def main():
    decision = ask_user("DECIDE", "RSA: type 1 to add file or type 2 to verify")

    if decision == str(1):
        execfile("RSAencr.py")
    elif decision == str(2):
        execfile("RSAdecr.py")
    else:
        exit(4)

main()