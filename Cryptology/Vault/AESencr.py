from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox
from Crypto.Cipher import AES
import base64
import os

# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

def pop_window(title, message):
    tkMessageBox.showinfo(title, message)

def select_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename

def ask_user(prompt, command):
    root = Tkinter.Tk()
    var = tkSimpleDialog.askstring(str(prompt), str(command))
    #print var
    return var

def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING


def encode_aes(c, s):
    return base64.b64encode(c.encrypt(pad(s)))


def main():

    userInput = ask_user("DECIDE", "TYPE 1 TO ENCRYPT, TYPE 2 TO DECRYPT")
    print userInput
    if userInput == str(1):
        # ASK USER TO INPUT KEY
        key_question = ask_user("DECIDE", "Press 1 to Generate key or Press 2 select existing key?")
        if key_question == str(1):
            # GENERATE A RANDOM SECRET KEY 16 bytes
            secret = os.urandom(BLOCK_SIZE)
            publicKeyName = ask_user("TYPE A KEY NAME", "type keyname + .pem 'mykey.pem' and press 'OK':")
            file = open(publicKeyName, 'w')
            public_key = secret
            file.writelines(public_key)
            file.close()
        elif key_question == str(2):
            pop_window("SELECT Key", "Select a key from your computer to encrypt")
            publicKeyName = select_file()
        else:
            exit(2)

        # ASK THE USER TO INPUT THE FILE TO ENCRYPT
        cipher = AES.new(open(publicKeyName, 'r').readline())

        pop_window("SELECT FILE", "Select a Message.txt from your computer to encrypt")
        msg = select_file()
        m = open(msg, 'r').readlines()
        # REMOVE THE \n FROM ALL ELEMENTS IN THE LIST
        m = map(lambda s: s.strip(), m)

        print m
        message = ""
        for items in m:
            message += "%s\n" % encode_aes(cipher, str(items))
            print ("%s\n" % items)

        encoded = encode_aes(cipher, str(m))

        print 'Encrypted string:', message

        # ASK THE USER TO INPUT THE NAME OF THE NEW CIPHER TEXT
        filename = ask_user("TYPE YOUR CIPHERTEXT NAME", "type encrypted message 'Ciphertext.txt' and press 'OK':")
        f = open(filename, 'w')
        public_key = message
        f.writelines(public_key)
        f.close()
    elif userInput == str(2):
        execfile("AESdecr.py")
    else:
        exit(3)


main()
