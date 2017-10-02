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
    h.update(str(message))
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

    # it should open the private key you selected and compare with the hash of the secret
    f = open(secret_file, 'r')
    signature2 = hash_sha512(f.read())
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

        if Counter(signature2) == Counter(m[index]):
            print "VERIFIED FILE"
            # pop_window("SELECT CIPHERTEXT", "CIPHERTEXT.TXT from your computer")
            # filename = select_file()
            # print(filename)
            file = open(secret_file, 'r')
            ecrypted_message = file.readline()
            file.close()

            pop_window("SELECT PRIVATE KEY", "prKey.PEM from your computer")
            privateKeyname = select_file()

            f = open(privateKeyname, 'r')
            # passphrase is password
            password = ask_user("Type Key password", "Please type your password: ")
            priv_key_obj = RSA.importKey(f.read(), passphrase=password)

            # DECRYPT THE MESSAGE
            decrypted = priv_key_obj.decrypt(ast.literal_eval(str(ecrypted_message)))
            f.close()
            # DISPLAY THE DECRYPTED MESSAGE
            print 'DECRYPTED', decrypted
            signatureFound = True
            # stop the loop
            break
        # if the signature is not in the secret increment by one
        index += 1
    if signatureFound == False:
        print "Sorry wrong keys"


main()