import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'message')

# NAME: Antonino Sauleo
# ASSIGNMENT 1
# SECURE PROGRAMMING


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
    key = filer_unwanted_key(key)
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
        message = filer_unwanted(message)
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
        print("The encrypted message is: " + str(read_file()) + "\n")
        # RETURN TO MAIN
        main()

    # TO DECRYPT A MESSAGE
    elif decision == str(2):
        # GET THE CIPHER TEXT FROM THE FILE
        encrypted_m = filer_unwanted(read_file())
        # DISPLAY THE CIPHER TEXT
        print encrypted_m
        # SPLIT THE LIST INTO TWO CHARACTERS
        cipher_text = []
        cipher_text = make_digraph(cipher_text, encrypted_m)
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


# OPEN FILE, READ AND RETURN THE STRING/LIST
def read_file():
    with open(filename) as f:
        read_data = f.readline()
        return read_data


# PRINT THE MATRIX IN A 5 X 5 SQUARE
def print_matrix(matrix):
    print " ", " ".join([str(character) for character in xrange(len(matrix))])
    for enumerated, character in enumerate(matrix):
        print enumerated, " ".join(character)


# GET COORDINATES INSIDE THE MATRIX, METHOD TAKES TWO ARGUMENTS DIGRAPH AND MATRIX
def get_coordinates(digraph, key_matrix):
    # CREATE EMPTY LIST (used to append the matches)
    coordinates = []
    # GET THE COORDINATES OF THE CHARACTER IN DIGRAPH INSIDE MATRIX/KEY
    # RUNS TWO TIMES FOR EACH ELEMENT OF DIGRAPH
    for char in digraph:
        for x in range(5):
            for y in range(5):
                if key_matrix[x][y] == char:
                    coordinates.append((x, y))
    #print coordinates
    return coordinates


def decrypt(message, key_matrix):
    plain_text = []
    for digraph in message:
        swap = []
        coordinates = get_coordinates(digraph, key_matrix)
        # IF DIGRAPH IS ON THE SAME X AXIS
        if coordinates[0][0] == coordinates[1][0]:
            x = coordinates[0][0]
            y = (coordinates[0][1] - 1) % 5
            swap.append((x, y))
            x = coordinates[1][0]
            y = (coordinates[1][1] - 1) % 5
            swap.append((x, y))
        # IF DIGRAPH IS ON SAME Y AXIS
        elif coordinates[0][1] == coordinates[1][1]:
            x = ((coordinates[0][0] - 1) % 5)
            y = (coordinates[0][1])
            swap.append((x, y))
            x = ((coordinates[1][0] - 1) % 5)
            y = coordinates[1][1]
            swap.append((x, y))
        # IF DIGRAPH IS ON DIFFERENT X AND Y AXIS
        else:
            x = coordinates[0][0]
            y = coordinates[1][1]
            swap.append((x, y))
            x = coordinates[1][0]
            y = coordinates[0][1]
            swap.append((x, y))
        # APPEND THE SWAPPED CHARACTERS (REVERSED) IN THE PLAIN TEXT
        for x, y in swap:
            plain_text.append(key_matrix[x][y])
    return plain_text


def encrypt(message, key_matrix):
    cipher_text = []
    for d in message:
        swap = []
        coordinates = get_coordinates(d, key_matrix)
        # IF DIGRAPH IS ON THE SAME X AXIS
        if coordinates[0][0] == coordinates[1][0]:
            x = coordinates[0][0]
            y = (coordinates[0][1] + 1) % 5
            swap.append((x, y))
            x = coordinates[1][0]
            y = (coordinates[1][1] + 1) % 5
            swap.append((x, y))
        # IF DIGRAPH IS ON SAME Y AXIS
        elif coordinates[0][1] == coordinates[1][1]:
            x = ((coordinates[0][0] + 1) % 5)
            y = (coordinates[0][1])
            swap.append((x, y))
            x = ((coordinates[1][0] + 1) % 5)
            y = coordinates[1][1]
            swap.append((x, y))
        # IF DIGRAPH IS ON DIFFERENT X AND Y AXIS
        else:  # digraph lies on different x & y axis
            x = coordinates[0][0]
            y = coordinates[1][1]
            swap.append((x, y))
            x = coordinates[1][0]
            y = coordinates[0][1]
            swap.append((x, y))
        # APPEND THE SWAPPED CHARACTERS IN THE CIPHER TEXT
        for x, y in swap:
            cipher_text.append(key_matrix[x][y])
    return cipher_text


# REMOVE UNWANTED CHARACTERS FROM A MESSAGE
def filer_unwanted(message):
    # ALL CHARACTERS TO LOWER CASE
    message.lower()
    # LIST OF UNWANTED CHARACTERS
    unwanted = ("!,.?#!*&@$% ^&*()<>{}[]\/'1234567890")
    unwated_j = ("jJ")
    # FILTER THE MESSAGE, REPLACE 'j' WITH 'i'
    newmessage = message
    for char in message:
        if any(char == unwantedChar for unwantedChar in unwanted):
            newmessage = newmessage.replace(char, "")
        if any(char == unwated for unwated in unwated_j):
            newmessage = newmessage.replace(char, "i")
    # RETURN THE FILTERED MESSAGE
    return newmessage


# REMOVE UNWANTED CHARACTERS FROM A KEY
def filer_unwanted_key(key):
    # ALL CHARACTERS TO LOWER CASE
    key = key.lower()
    # ALPHABET WITH 25 CHARACTERS ('j' is not included)
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    # LIST OF UNWANTED CHARACTERS
    unwanted = ("!,.?#!*&@$% ^&*()<>{}Jj[]\/'1234567890")
    tmp = alphabet
    # FILTER THE MESSAGE, REMOVE 'j' IF IT EXISTS
    for char in key:
        if any(char == alphabetWord for alphabetWord in alphabet):
            tmp = tmp.replace(char, "")
        if any(char == unwantedChar for unwantedChar in unwanted):
            key = key.replace(char, "")
    key = key + tmp
    # RETURN THE KEY FOR THE MATRIX
    return key


# SPLIT THE LIST INTO TWO CHARACTERS
def make_digraph(empty_list, message_list):
    [empty_list.append(message_list[i:i + 2]) for i in range(0, len(message_list), 2)]
    return empty_list


# DOUBLE CHARACTERS ADD 'x' IN BETWEEN, IF IT'S ODD ADD 'z'.
def padding_and_doubles(digraph):
    # ADD 'x' IN BETWEEN LIST
    i = 0
    for e in range(len(digraph) / 2):
        if digraph[i] == digraph[i + 1]:
            digraph.insert(i + 1, 'x')
        i = i + 2
    # ADD 'z' IF IT'S ODD NUMBER
    if len(digraph) % 2 == 1:
        digraph.append("z")
    return digraph


# EXECUTE MAIN
main()
