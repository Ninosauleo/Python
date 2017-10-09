from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
from collections import Counter
from Tkinter import Tk
from tkFileDialog import askopenfilename
import ast
import os
import tkMessageBox
import Tkinter
import tkSimpleDialog
import tkMessageBox


fileDir = os.path.dirname(os.path.realpath('__file__'))


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


def hash_sha512(message):
    # SHA512 HASHING OF THE INPUT FILE
    h = SHA512.new()
    h.update(message)
    # digest() Return the binary (non-printable) digest of the message that has been hashed so far.
    # hexdigest() Return the printable digest of the message that has been hashed so far.
    signature = h.hexdigest()
    return signature


def read_file_all(file_name):
    filename = os.path.join(fileDir, str(file_name))
    with open(filename, 'r') as f:
        read_data = f.readlines()
        return read_data


def main():
    print "hello"
    # STEP TWO DECRYPTION:
    m = read_file_all("secret.txt")
    # REMOVE THE \n FROM ALL ELEMENTS IN THE LIST
    m = map(lambda s: s.strip(), m)

    pop_window("SELECT FILE FROM COMPUTER", "Please Select a file to decrypt")
    secret_file = select_file()
    # HASH THE FILE
    filename = open(secret_file, 'r').read()
    hashing = hash_sha512(filename)
    print hashing

    pop_window("SELECT PUBLIC KEY", "puKey.PEM from your computer")
    publicKeyName = select_file()

    f = open(publicKeyName, 'r')
    pubKeyObj = RSA.importKey(f.read())
    # ENCRYPT THE MESSAGE FROM FILE
    n = []
    signature2 = pubKeyObj.encrypt(str(hashing), 32)
    n.append("%s\n" % str(signature2))
    n = map(lambda s: s.strip(), n)

    print "This is signature 2: "
    print n[0]

    f.close()


   # LOOP THROUGH ALL OF THE LIST
    index = 0
    signatureFound = False
    while(index < (len(m) -1)):
        print "index at : " + str(index)
        print m[index]
        index += 1
        print "plus one is " + str(index)
        print m[index]

        print "This is counter for signature 2"
        print Counter(n[0])
        print "\nThis is counter for m[secret]"
        print Counter(m[index])
        if Counter(n[0]) == Counter(m[index]):
            signatureFound = True
            print "VERIFIED FILE"
            break

    if signatureFound == False:
        print "Sorry file is not verified"
        print secret_file


main()