import random
import sys
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'PLknowledgebase.txt')
with open(filename) as file:
    content = file.readlines()

print(content)


print("formulas")



def evaluate(s, p, q, r):
    if type(s) is str:
        if s == "P":
            return p
        if s == "Q":
            return q
        if s == "R":
            return r
    #In case if ->
    elif type(s) is list and s[0] == "if":
        if (evaluate(s[1],p,q,r) == True) and (evaluate(s[2],p,q,r) == True):
            return True
        elif(evaluate(s[1],p,q,r) == True) and (evaluate(s[2],p,q,r) == False):
            return False
        elif (evaluate(s[1], p, q, r) == False) and (evaluate(s[2], p, q, r) == True):
            return True
        elif (evaluate(s[1], p, q, r) == False) and (evaluate(s[2], p, q, r) == False):
            return True
        ## Fill in the remaining cases
    # In case if &
    elif type(s) is list and s[0] == "and":
        if (evaluate(s[1],p,q,r) == True) and (evaluate(s[2],p,q,r) == True):
            return True
        else:
            return False
    # In case if |
    elif type(s) is list and s[0] == "or":
        if (evaluate(s[1],p,q,r) == True) or (evaluate(s[2],p,q,r) == True):
            return True
        else:
            return False
    # In case if !
    elif type(s) is list and s[0] == "not":
        if (evaluate(s[1],p,q,r) == True):
            return False
        elif(evaluate(s[1],p,q,r) == False):
            return True

    else:
        print "Error"





for l in content:
     print repr (evaluate(eval(l.strip()),True,True,False))

     #['or', ['not', ['if', 'P', 'Q']], ['if', 'R', 'P']]