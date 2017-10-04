from Tkinter import Tk
from tkFileDialog import askopenfilename
import tkMessageBox
import tkSimpleDialog
import tkMessageBox
import Tkinter
from Crypto.Cipher import AES
import base64


# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'


def ask_user(prompt, command):
    root = Tkinter.Tk()
    var = tkSimpleDialog.askstring(str(prompt), str(command))
    #print var
    return var


def pop_window(title, message):
    tkMessageBox.showinfo(title, message)


def select_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return filename


def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING


def decode_aes(c, e):
    e = str(e)
    return c.decrypt(base64.b64decode(e)).rstrip(PADDING)



pop_window("SELECT key", "Select a KEY.PEM from your computer to encrypt")
key = select_file()

cipher = AES.new(open(key, 'r').readline())

# OPEN FILE TO DECRYPT
pop_window("SELECT FILE", "Select a Message.txt from your computer to decrypt")
cmsg = select_file()
m = open(cmsg, 'r').readlines()
# REMOVE THE \n FROM ALL ELEMENTS IN THE LIST
m = map(lambda s: s.strip(), m)
print m
message = ""

deleteFile = ask_user("DO YOU WANT TO OVERRIDE THE ENCRYPTED FILE?", "TYPE 1 TO OVERRIDE OR TYPE 2 TO CREATE A NEW ONE")
if deleteFile == str(1):
    # WRITE DECRYPTED MESSAGE back into file
    f = open(cmsg, 'w')
    for items in m:
        message += "%s\n" % decode_aes(cipher, str(items))
    f.writelines(message)
    f.close()
elif deleteFile == str(2):
    filename = ask_user("TYPE YOUR DECRYPTED FILE NAME", "type message + format (.pdf .txt, etc...)\n'Ciphertext.txt' and press 'OK':")
    f = open(filename, 'w')
    for items in m:
        message += "%s\n" % decode_aes(cipher, str(items))
    f.writelines(message)
    f.close()




# decode the encoded string
#decoded = decode_aes(cipher, str(open(cmsg, 'r').readlines()))
print 'Decrypted string:', message



