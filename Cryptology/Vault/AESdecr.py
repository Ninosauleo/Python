from Tkinter import Tk
from tkFileDialog import askopenfilename
import tkMessageBox
from Crypto.Cipher import AES


def pop_window(title, message):
    tkMessageBox.showinfo(title, message)


def select_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename


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



# SELECT ANY FILE
pop_window("SELECT key", "Select a KEY.PEM from your computer to encrypt")
selected_key = select_file()

# ASK THE USER TO INPUT THE FILE TO ENCRYPT
key = open(selected_key, 'rb').readline()


# OPEN FILE TO DECRYPT
pop_window("SELECT FILE", "Select a Message.txt from your computer to decrypt")
cmsg = select_file()

# DECRYPT THE FILE
decrypt_file(cmsg, key)

# RETURN TO MAIN MENU
execfile("AESencr.py")



