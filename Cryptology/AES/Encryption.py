from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox
from Crypto.Cipher import AES
import os
from Crypto import Random
from Crypto.Hash import SHA512




BLOCK_SIZE = 16


def hash_sha512(message):
    # SHA512 HASHING OF THE INPUT FILE
    h = SHA512.new()
    h.update(str(message))
    # digest() Return the binary (non-printable) digest of the message that has been hashed so far.
    # hexdigest() Return the printable digest of the message that has been hashed so far.
    signature = h.hexdigest()
    return signature

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
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


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


def main():
    # ASK TO USER FOR INPUT IN MENU
    userInput = ask_user("DECIDE", "TYPE 1 TO ENCRYPT, TYPE 2 TO DECRYPT.\n In order to exit type anything else.")
    # FIRST START WITH SELECTING OR CREATING THE KEY
    if userInput == str(1):
        # ASK USER TO INPUT KEY
        key_question = ask_user("DECIDE", "Press 1 to Generate key or Press 2 select existing key?")
        if key_question == str(1):
            # GENERATE A RANDOM SECRET KEY 16 BYTES
            secret = os.urandom(BLOCK_SIZE)
            publicKeyName = ask_user("TYPE A KEY NAME", "type keyname + .pem 'mykey.pem' and press 'OK':")
            file = open(publicKeyName, 'wb')
            public_key = secret
            file.writelines(public_key)
            file.close()
        elif key_question == str(2):
            # SELECT ANY EXISTING KEY
            pop_window("SELECT Key", "Select a key from your computer to encrypt")
            publicKeyName = select_file()
        else:
            exit(2)

        # ASK THE USER TO INPUT THE FILE TO ENCRYPT
        key = open(publicKeyName, 'rb').readline()

        # SELECT ANY DESIRED FILE
        pop_window("SELECT FILE", "Select a Message.txt from your computer to encrypt")
        msg = select_file()
        # RUN ENCRYPTION
        encrypt_file(msg, key)
        # RETURN TO MAIN MENU
        main()

    elif userInput == str(2):
        execfile("decryption.py")
    else:
        exit(3)


main()
