from Tkinter import Tk
from tkFileDialog import askopenfilename
import tkMessageBox
from Crypto.Cipher import AES
import base64


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


def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING


def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).rstrip(PADDING)



pop_window("SELECT key", "Select a KEY.PEM from your computer to encrypt")
key = select_file()

cipher = AES.new(open(key, 'r').readline())

pop_window("SELECT FILE", "Select a Message.txt from your computer to decrypt")
cmsg = select_file()


# decode the encoded string
decoded = decode_aes(cipher, open(cmsg, 'r').readline())
print 'Decrypted string:', decoded