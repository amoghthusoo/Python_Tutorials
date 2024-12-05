from keyword import kwlist

_input = "print"

i = 0 
while(i < len(kwlist)):
    if(_input == kwlist[i]):
        print("The entered word is a keyword.")
        quit()
    i += 1
else:
    print("The entered word is NOT a keyword.")