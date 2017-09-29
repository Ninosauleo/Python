from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
from collections import Counter
from Tkinter import Tk
from tkFileDialog import askopenfilename
import ast
import os
import tkMessageBox

fileDir = os.path.dirname(os.path.realpath('__file__'))


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


def main():
    decision = str(raw_input(" Would you like to generate an RSA key type 1 or select an existing one type 2 \n"))

    if decision == str(1):
        # GENERATE RANDOM NUMBER FOR KEY
        random_generator = Random.new().read
        # CREATE PUBLIC-KEY AND PRIVATE KEY
        key = RSA.generate(1024, random_generator)
        # BINARY PUBLIC KEY
        privateKeyname = raw_input("\n Please type the keyname + .pem 'myprivatekey.pem' and press 'Enter': \n")

        f = open(privateKeyname, 'w')
        private_key = key.exportKey('PEM', '123', pkcs=1)
        f.writelines(private_key)
        f.close()

        publicKeyName = raw_input("\n Please type keyname + .pem 'mypublickey.pem' and press 'Enter': \n")
        file = open(publicKeyName, 'w')
        public_key = key.publickey().exportKey('PEM')
        file.writelines(public_key)
        file.close()
    else:
        print "nothing to do here yet"
        pop_window("SELECT PUBLIC KEY", "puKey.PEM from your computer")
        publicKeyName = select_file()
        pop_window("SELECT PRIVATE KEY", "prKey.PEM from your computer")
        privateKeyname = select_file()



    # READ INPUT FROM FILE
    pop_window("SELECT FILE", "FILE.TXT from your computer")
    filename = select_file()
    print(filename)
    file = open(filename, 'r')
    send_message = file.readline()

    # HASH FUNCTION / HASH PRIVATE KEY
    # it should open the file you selected for the key /any private key file
    f = open(privateKeyname, 'r')
    signature = hash_sha512(f.read())
    print "Hash"
    print signature
    f.close()

    # IMPORT KEY / depends if it's the auto/generated or the selected
    # ask to select a public key to import and after selecting you encrypt
    f = open(publicKeyName, 'r')
    pubKeyObj = RSA.importKey(f.read())
    print "this is pubKey obj: " + str(pubKeyObj)
    #publickey = key.publickey()  # pub key export for exchange

    # ENCRYPT THE MESSAGE FROM FILE
    encrypted = pubKeyObj.encrypt(send_message, 32)
    f.close()
    # DISPLAY ENCRYPTED MESSAGE
    print 'encrypted message:', encrypted

    # OPEN FILE TO STORE SECRET MESSAGE
    cipher_text = raw_input("\n Please type the cipher_text (ciphertextname +.txt): \n")
    f = open(cipher_text, 'w')
    # WRITE THE CIPHER TEXT IN THE MESSAGE
    f.write(str(encrypted))
    # CLOSE FILE
    f.close()

    # APPEND SIGNATURE TO SECRET FILE IN FORMAT FILE_NAME : SIGNATURE
    f = open('secret.txt', 'w')
    file_name = filename
    secret_list = []
    secret_list.append(str(file_name))
    secret_list.append(str(signature))
    # ASK IF FILE_NAME IS THE CIPHER TEXT? OR IF YOU NEED TO ADD ALL THE PATH NAME
    # ALSO ASK IF WE NEED TO RSA AND HASH TOGETHER OR SEPARATE
    for items in secret_list:
        f.writelines("%s\n" % items)
    f.close()


main()