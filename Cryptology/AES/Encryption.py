import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import sys
from Tkinter import *
import Tkinter, tkFileDialog


def main():
    print("Hello! Please select a file from your computer to encrypt or decrypt.")
    root = Tkinter.Tk()
    root.update()  # hides tkinter window


    file_path = tkFileDialog.askopenfilename()
    print(file_path)
    inputFile = open(file_path, 'r')
    myFile = inputFile.read()
    myFile = myFile.split()
    inputFile.close()
    print("This is my file: ", myFile)
    # check above

    # ask user if they want to create a key or find the file somewhere
    print("Please select the text file where your secret key is hidden: ")
    root = Tkinter.Tk()
    root.update()  # hides tkinter window
    file_path_key = tkFileDialog.askopenfilename()
    inputKey = open(file_path_key, 'r')
    myKey = inputKey.read()
    inputFile.close()
    print(myKey)

    iv = Random.new().read(AES.block_size)
    print AES.block_size
    cipher = AES.new(myKey, AES.MODE_CFB, iv)

    msg = iv + cipher.encrypt(str(myFile))

    outputFile = open('cipher.txt', 'w')
    outputFile.write(msg)
    outputFile.close()


    print "the cipher text is " + msg

    decrypted = cipher.decrypt(msg)

    print decrypted





    # outputFile = open('encryption.txt', 'w')
    # outputFile.write(str(cipherText.encode('hex')))
    # outputFile.close()
    # print("Your encrypted file looks like: ", cipherText.encode('hex'))
    # print("Your encrypted file is saved to the desktop.")


    # decodedObj = AES.new(key, AES.MODE_ECB.IV = IV)
    # newFile = (outputFile, 'r')
    # newFileDecrypt = newFile.read()
    # newFileDecrypt = newFileDecrypt.split()
    # decodedText = decodedObj.decrypt(cipherText('hex'))
    # print(decodedText)


main()
