import random
import sys
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'PLknowledgebase.txt')
with open(filename) as file:
    content = file.readlines()

print(content)


print("formulas")



def infix(s):
    if type(s) is str:
        return s
    elif type(s) is list and s[0] == "if":
        return [ infix(s[1]),"->",infix(s[2])]
    elif type(s) is list and s[0] == "and":
        return [ infix(s[1]),"^",infix(s[2])]
    elif type(s) is list and s[0] == "or":
        return [ infix(s[1]),"|",infix(s[2])]
    elif type(s) is list and s[0] == "not":
        return [ "!", infix(s[1])]
    else:
        print 'Something went wrong'





for l in content:
     print repr (infix(eval(l.strip())))

     #(if P then not Q) or (if R then P)