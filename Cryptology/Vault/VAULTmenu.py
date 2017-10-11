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


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)



def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name, 'wb') as fo:
        fo.write(enc)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")


def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        cipher_text = fo.read()
    dec = decrypt(cipher_text, key)
    with open(file_name, 'wb') as fo:
        fo.write(dec)




def main():
    decision = ask_user("DECIDE", "DO YOU WANT TO USE RSA type 1 to add/verify a file \n OR AES type 2 to encrypt and decrypt?")

    if decision == str(1):
        execfile("RSAmenu.py")
    elif decision == str(2):
        execfile("AESencr.py")
    else:
        exit(4)

main()