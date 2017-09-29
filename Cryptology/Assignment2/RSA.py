from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random
from collections import Counter
from Tkinter import Tk
from tkFileDialog import askopenfilename
import ast
import os

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

def hash_sha512(message):
    # SHA512 HASHING OF THE INPUT FILE
    h = SHA512.new()
    h.update(str(message))
    # digest() Return the binary (non-printable) digest of the message that has been hashed so far.
    # hexdigest() Return the printable digest of the message that has been hashed so far.
    signature = h.hexdigest()
    return signature


def main():

    # GENERATE RANDOM NUMBER FOR KEY
    random_generator = Random.new().read

    # CREATE PUBLIC-KEY AND PRIVATE KEY
    key = RSA.generate(1024, random_generator)
    # BINARY PUBLIC KEY
    f = open('myprivatekey.pem', 'w')
    private_key = key.exportKey('PEM')
    f.writelines(private_key)
    f.close()

    # READ INPUT FROM FILE
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print "\n Hello, user. " "\n \n INPUT TEXT Please type in the path to your file .txt and press 'Enter': "
    print(filename)
    file = open(filename, 'r')
    send_message = file.readline()
    # HASH FUNCTION
    # it should open the file you selected for the key /any private key file
    f = open('myprivatekey.pem', 'r')
    signature = hash_sha512(f.read())
    print "Hash"
    print signature
    f.close()


    f = open('mypublickey.pem', 'w')
    public_key = key.publickey().exportKey('PEM')
    f.writelines(public_key)
    f.close()

    # IMPORT KEY
    # ask to select a public key to import and after selecting you encrypt
    f = open('mypublickey.pem', 'r')
    pubKeyObj = RSA.importKey(f.read())
    print "this is pubKey obj: " + str(pubKeyObj)
    #publickey = key.publickey()  # pub key export for exchange

    # ENCRYPT THE MESSAGE FROM FILE
    encrypted = pubKeyObj.encrypt(send_message, 32)
    f.close()
    # DISPLAY ENCRYPTED MESSAGE
    print 'encrypted message:', encrypted

    # OPEN FILE TO STORE SECRET MESSAGE
    f = open('encryption.txt', 'w')
    # WRITE THE CIPHER TEXT IN THE MESSAGE
    f.write(str(encrypted))
    # CLOSE FILE
    f.close()

    # APPEND SIGNATURE TO SECRET FILE IN FORMAT FILE_NAME : SIGNATURE
    f = open('secret.txt', 'w')
    file_name = "encryption.txt : "
    secret_list = []
    secret_list.append(str(file_name))
    secret_list.append(str(signature))
    # ASK IF FILE_NAME IS THE CIPHER TEXT? OR IF YOU NEED TO ADD ALL THE PATH NAME
    # ALSO ASK IF WE NEED TO RSA AND HASH TOGETHER OR SEPARATE
    for items in secret_list:
        f.writelines("%s\n" % items)
    f.close()

    # STEP TWO DECRYPTION:
    m = read_file_all("secret.txt")
    # REMOVE THE \n FROM ALL ELEMENTS IN THE LIST
    m = map(lambda s: s.strip(), m)
    print "Signature in secret is"
    print m[1]

    # it should open the private key you selected and compare with the hash of the secret
    f = open('myprivatekey.pem', 'r')
    signature2 = hash_sha512(f.read())
    f.close()
    print "new hash"
    print signature2

    # ask if we need PKCS1_v1_5
    # https://stackoverflow.com/questions/6350031/how-to-verify-in-pycrypto-signature-created-by-openssl
    # compare hash of signature
    if Counter(signature2) == Counter(m[1]):
        print "VERIFIED private key SHA512"
    else:
        print Counter(signature2)
        print Counter(m[1])

    # now verify the decryption with the RSA method IF VERIFIED THEN

        # READ ENCRYPTED MESSAGE
    encr = read_file_line("encryption.txt")

    f = open('myprivatekey.pem', 'r')
    privKeyObj = RSA.importKey(f.read())

    # DECRYPT THE MESSAGE
    decrypted = privKeyObj.decrypt(ast.literal_eval(str(encr)))
    f.close()
    # DISPLAY THE DECRYPTED MESSAGE
    print 'DECRYPTED', decrypted

    # DECRYPTED MESSAGE
    f = open('encryption.txt', 'r')
    message = f.read()
    f.close()

    # WRITE DECRYPTED MESSAGE AND ENCRYPTED MESSAGE
    # OPEN ENCRYPTED WRITE ENCRYPTED MESSAGE AND DECRYPTED
    f = open('decryption.txt', 'w')
    f.write(str(message))
    f.write(str(decrypted))
    f.close()


main()