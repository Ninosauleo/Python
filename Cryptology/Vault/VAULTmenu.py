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
from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox
from Crypto.Cipher import AES
import base64
import os
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox
import base64
import os


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

# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

PADDING = '{'


def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING


def encode_aes(c, s):
    return base64.b64encode(c.encrypt(pad(s)))




def main():
    decision = ask_user("DECIDE", "DO YOU WANT TO USE RSA OR AES?")

    if decision == str(1):
        execfile("RSAmenu.py")
    elif decision == str(2):
        execfile("AESencr.py")
    else:
        exit(4)

main()