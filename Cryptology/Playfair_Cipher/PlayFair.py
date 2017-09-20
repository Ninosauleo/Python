import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'workfile')


def print_matrix(matrix):
    for counter in range(5):
        print "%c %c %c %c %c" % (
            matrix[counter][0], matrix[counter][1], matrix[counter][2], matrix[counter][3], matrix[counter][4])
    print "\n"


def getCoordinates(digraph, key_matrix):
    coords = []
    for char in digraph:
        for x in range(5):
            for y in range(5):
                if key_matrix[x][y] == char:
                    coords.append((x, y))
    return coords


def decrypt(message, key_matrix):
    plaintext = []
    for digraph in message:
        swap = []
        coords = getCoordinates(digraph, key_matrix)
        if coords[0][0] == coords[1][0]:  # digraph lies on same x axis
            x, y = ((coords[0][0], (coords[0][1] - 1) % 5))
            swap.append((x, y))
            x, y = ((coords[1][0], (coords[1][1] - 1) % 5))
            swap.append((x, y))
        elif coords[0][1] == coords[1][1]:  # digraph lies on same y axis
            x, y = (((coords[0][0] - 1) % 5), coords[0][1])
            swap.append((x, y))
            x, y = (((coords[1][0] - 1) % 5), coords[1][1])
            swap.append((x, y))
        else:  # digraph lies on different x & y axis
            swap.append((coords[0][0], coords[1][1]))
            swap.append((coords[1][0], coords[0][1]))
        for x, y in swap:
            plaintext.append(key_matrix[x][y])
    return plaintext


def encrypt(message, key_matrix):
    ciphertext = []
    for d in message:
        swap = []
        coords = getCoordinates(d, key_matrix)
        if coords[0][0] == coords[1][0]:  # digraph lies on same x axis
            x, y = ((coords[0][0], (coords[0][1] + 1) % 5))
            swap.append((x, y))
            x, y = ((coords[1][0], (coords[1][1] + 1) % 5))
            swap.append((x, y))
        elif coords[0][1] == coords[1][1]:  # digraph lies on same y axis
            x, y = (((coords[0][0] + 1) % 5), coords[0][1])
            swap.append((x, y))
            x, y = (((coords[1][0] + 1) % 5), coords[1][1])
            swap.append((x, y))
        else:  # digraph lies on different x & y axis
            swap.append((coords[0][0], coords[1][1]))
            swap.append((coords[1][0], coords[0][1]))
        for x, y in swap:
            ciphertext.append(key_matrix[x][y])
    return ciphertext


def filerUnwanted(message):
    # all characters to lower case
    message.lower()
    # remove all the unwanted characters
    unwanted = ("!,.?#!*&@$% ^&*()<>{}[]\/'1234567890")
    # create a message with the previous and one replace j with i
    newmessage = message
    for char in message:
        if any(char == unwantedChar for unwantedChar in unwanted):
            newmessage = newmessage.replace(char, "")
        if any('j' == unwantedChar for unwantedChar in newmessage):
            newmessage = newmessage.replace(char, "i")
    return newmessage


def filerUnwantedKey(key):
    # All characters to lower case
    key = key.lower()
    # The alphabet does not include a J so it's 25 characters
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    #filter all bad characters
    unwanted = ("!,.?#!*&@$% ^&*()<>{}Jj[]\/'1234567890")
    tmp = alphabet
    for char in key:
        if any(char == alphabetWord for alphabetWord in alphabet):
            tmp = tmp.replace(char, "")
        if any(char == unwantedChar for unwantedChar in unwanted):
            key = key.replace(char, "")
    key = key + tmp
    return key


def make_digraph(list, messageList):
    [list.append(messageList[i:i + 2]) for i in range(0, len(messageList), 2)]
    return list


def padding_and_doubles(digraph):
    # divide the string into strings of two chars
    i = 0
    for e in range(len(digraph) / 2):
        if digraph[i] == digraph[i + 1]:
            digraph.insert(i + 1, 'x')
        i = i + 2
    # If it is odd digit, add an "z" for padding
    if len(digraph) % 2 == 1:
        digraph.append("z")
    return digraph


def main():
    # GET THE USER INPUT
    decision = str(raw_input("Would you like to encrypt or decrypt this message? Type 1 for encrypt and 2 for decrypt or 3 for exit: \n"))

    # EXIT THE PROGRAM
    if decision == str(3):
        exit()
    # INCORRECT INPUT
    if ((decision != str(1)) and (decision != str(2))):
        print "Incorrect input\n"
        main()

    # 1 KEY CONSTRAINTS: KEY CANNOT HAVE THE SAME LETTER TWICE and not J.
    key = str(raw_input("PLEASE ENTER A KEY (no duplicate letters) \n"))
    key = filerUnwantedKey(key)
    # KEY TO LOWER CASE
    key = key.lower()
    for char in key:
        if key.count(char) > 1:
            print "Wrong Key try again \n"
            main()
    # SHOW THE NEW ALPHABET
    print ("This is the new match in alphabet " + key)

    # CREATE MATRIX
    test_matrix = [key[(5 * i):(5 * i + 5)] for i in range(5)]
    # SHOW MATRIX
    print_matrix(test_matrix)

    # TO WRITE THE ENCRYPTION:
    if decision == str(1):
        # OPEN THE FILE TO WRITE
        f = open(filename, 'w')
        # GET THE INPUT
        message = str(raw_input("Please enter your plaintext message here: \n"))
        # VERIFY THAT THE INPUT IS 3 OR MORE CHARACTERS
        if len(message) < 3:
            print "Message is too short type at least 3 chars \n"
            main()
        # FILTER THE UNWANTED CHARACTERS
        message = filerUnwanted(message)
        # LOWER CASE (because it didn't return lower case the function)
        message = message.lower()
        # SHOW THE FILTERED MESSAGE
        print ("This is the filtered message " + message)

        # TRANSFORM THE STRING TO A CHAR LIST
        digraph = list(message)
        print digraph

        # DOUBLE CHARACTERS ADD 'x' IN BETWEEN, IF IT'S ODD ADD 'z'.
        digraph = padding_and_doubles(digraph)

        # SPLIT THE LIST INTO TWO CHARACTERS
        new = []
        new = make_digraph(new, digraph)
        # SHOW THE NEW LIST WITH TWO ELEMENTS FOR EACH INDEX
        print new

        # ENCRYPT THE MESSAGE
        cipher_text = encrypt(new, test_matrix)

        # WRITE THE CIPHER TEXT TO THE FILE
        f.write(str(cipher_text))
        # CLOSE THE FILE
        f.close()
        # SHOW THE CIPHER TEXT FROM THE FILE
        print("The encrypted message is: " + str(readFile()) + "\n")
        # RETURN TO MAIN
        main()

    # TO DECRYPT A MESSAGE
    elif decision == str(2):
        # GET THE CIPHER TEXT FROM THE FILE
        encryptedM = filerUnwanted(readFile())
        # DISPLAY THE CIPHER TEXT
        print encryptedM
        # SPLIT THE LIST INTO TWO CHARACTERS
        cipher_text = []
        cipher_text = make_digraph(cipher_text, encryptedM)
        # SHOW THE NEW LIST WITH TWO ELEMENTS FOR EACH INDEX
        print cipher_text
        # DECRYPT THE CIPHER TEXT
        plain_text = decrypt(cipher_text, test_matrix)
        # DISPLAY PLAIN TEXT
        print ("The decrypted message is: %s" % ''.join(plain_text))
        # RETURN TO MAIN
        main()

    # SOMETHING WENT WRONG
    else:
        print("Sorry, something went wrong \n")
        main()


def readFile():
    with open(filename) as f:
        read_data = f.readline()
        return read_data


main()
