from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tkinter
import tkSimpleDialog
import tkMessageBox


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
    h.update(message)
    # digest() Return the binary (non-printable) digest of the message that has been hashed so far.
    # hexdigest() Return the printable digest of the message that has been hashed so far.
    signature = h.hexdigest()
    return signature


def main():
    decision = ask_user("DECIDE", "Would you like to generate an RSA key type 1 or select an existing one type 2 ")
    if decision == str(1):
        # GENERATE RANDOM NUMBER FOR KEY
        random_generator = Random.new().read
        # CREATE PUBLIC-KEY AND PRIVATE KEY
        key = RSA.generate(1024, random_generator)
        # BINARY PUBLIC KEY
        privateKeyname = ask_user("TYPE PRIVATEKEYNAME.PEM", "Please type the keyname + .pem 'myprivatekey.pem' and press 'Enter': ")
        f = open(privateKeyname, 'w')
        password = ask_user("Type Key password", "Please create your password: ")
        private_key = key.exportKey('PEM', password, pkcs=1)
        f.writelines(private_key)
        f.close()

        publicKeyName = ask_user("TYPE PUBLICKEYNAME.PEM", "Please type keyname + .pem 'mypublickey.pem' and press 'Enter':  ")
        file = open(publicKeyName, 'w')
        public_key = key.publickey().exportKey('PEM')
        file.writelines(public_key)
        file.close()
    elif decision == str(2):
        pop_window("SELECT PUBLIC KEY", "puKey.PEM from your computer")
        publicKeyName = select_file()
        pop_window("SELECT PRIVATE KEY", "prKey.PEM from your computer")
        privateKeyname = select_file()
    else:
        exit(5)

    # READ INPUT FROM FILE
    pop_window("SELECT FILE", "FILE.TXT from your computer")
    file_name = select_file()

    # HASH THE FILE
    filename = open(file_name, 'r').read()
    hashing = hash_sha512(filename)
    #print hashing


    # IMPORT KEY / depends if it's the auto/generated or the selected
    # ask to select a public key to import and after selecting you encrypt
    f = open(publicKeyName, 'r')
    pubKeyObj = RSA.importKey(f.read())
    #print "this is pubKey obj: " + str(pubKeyObj)
    #publickey = key.publickey()  # pub key export for exchange

    # ENCRYPT THE MESSAGE FROM FILE
    signature = pubKeyObj.encrypt(str(hashing), 32)
    f.close()

    # APPEND THE SIGNATURE TO THE SECRET
    f = open('secret.txt', 'r')
    m = read_file_all("secret.txt")
    # REMOVE THE \n FROM ALL ELEMENTS IN THE LIST
    m = map(lambda s: s.strip(), m)
    #print m[0]
    #print m[1]
    f.close()

    # APPEND SIGNATURE TO SECRET FILE IN FORMAT FILE_NAME : SIGNATURE
    f = open('secret.txt', 'w')
    # secret_list = []
    # secret_list.append(str(file_name))
    # secret_list.append(str(signature))
    m.append(str(file_name))
    m.append(str(signature))
    # ASK IF FILE_NAME IS THE CIPHER TEXT? OR IF YOU NEED TO ADD ALL THE PATH NAME
    # ALSO ASK IF WE NEED TO RSA AND HASH TOGETHER OR SEPARATE
    for items in m:
        f.writelines("%s\n" % items)
    f.close()


main()