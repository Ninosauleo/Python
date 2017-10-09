from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox

def select_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename


def hash_sha512(message):
    # SHA512 HASHING OF THE INPUT FILE
    h = SHA512.new()
    h.update(message)
    # digest() Return the binary (non-printable) digest of the message that has been hashed so far.
    # hexdigest() Return the printable digest of the message that has been hashed so far.
    signature = h.hexdigest()
    return signature

# 5827f1475327fde165173e37d80a585d255e528db6975c848f338091231a6624f66aeae0e5c8c44514f3b66ca27e1949503f6b07213af4f4f4301298da118c37

def main():
    file_name = select_file()
    # ASK THE USER TO INPUT THE FILE TO ENCRYPT
    file = open(file_name, 'r').read()
    hashing = hash_sha512(file)
    print hashing


main()
