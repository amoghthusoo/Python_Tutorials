# eval() implementation in python.
# NOTE :- The program cannot handle any exceptions as of now.
# WARNING :- DEBUG can increase the processing time, meant for debugging purpose only.

import time
DEBUG = True            # DEBUG can be set to True or False.

# <---------------------------------Implementation of Stacks starts here----------------------------------------->

# push function for stack implementation
def push(stack : list, element : str) -> None:
    
    stack.append(element)
    return None

# pop function for stack implementation
def pop(stack : list) -> str:
    
    if len(stack) == 0:
        if DEBUG:
            print("\nDEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : OUT : Underflow")
        return None
    else:
        return stack.pop()
    
# isEmpty function for stack implementation
def isEmpty(stack : list) -> bool:
    
    if len(stack) == 0:
        if DEBUG:
            print("\nDEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : OUT : Stack is empty!")
        return True
    else:
        return False

# top function for stack implementation
def top(stack : list) -> None | str:
    
    if isEmpty(stack):
        return None
    else:
        return stack[-1]

# size function for stack implementation
def size(stack : list) -> int:
    return len(stack)

# <---------------------------------Implementation of Stacks ends here----------------------------------------->

# This returns the relative precedence of arithmetic operators
def precedence(operator : str) -> int:

    if operator in ['(', ')']:
        return -1                                   # Do not confuse with the actual precedence of brackets. {Added during debugging process.}
    elif operator in ['+', '-']:
        return 0
    elif operator in ['*', '/']:
        return 1

# This function returns whether the character is an operator or not    
def isOperator(character : str) -> bool:
    
    if character in ['+', '-', '*', '/', '(', ')']:             # '(' and ')' are added to the list during debugging process.         
        return True
    else:
        return False

# This function converts the input expression which is stored in a string into the list.
"""
It is found that processing the input expressiong directly only works with single digit numbers.
After this conversion, processing the inExp works for double digts as well and so on.
""" 
def converterStringList(inStr : str) -> list:

    if DEBUG:
        print()

    inExp = []
    i = 0
    j = 0                                       # Counter for the total number of indices in "inExp" list.                                   
    while i < len(inStr):
        if not isOperator(inStr[i]):
            if i == 0:
                inExp.append(inStr[i])
            elif isOperator(inExp[-1]):
                inExp.append(inStr[i])
                j += 1
            else:
                inExp[j] += inStr[i]
        elif isOperator(inStr[i]):
            inExp.append(inStr[i])
            j += 1
        i += 1

        if DEBUG:
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : inExp :", inExp)

    return inExp

# This function converts the infix expression to postfix expression.
def converterPostExp(inExp : list) -> list:

    if DEBUG:
        print()

    postExp = []
    stack = []

    for ch in inExp:

        if ch == '(':
            push(stack, ch)

        elif ch == ')':
            
            while True:
                popped_character = pop(stack)
                if popped_character == '(':
                    break
                else:
                    postExp.append(popped_character)

        elif isOperator(ch):

            if isEmpty(stack):
                push(stack, ch)

            elif (precedence(ch) <= precedence(top(stack))):            # Equality handles the associativity of operators from left to right

                while not isEmpty(stack):

                    top_character = top(stack)

                    if (precedence(top_character) < precedence(ch)):
                        break
                    else:
                        postExp += pop(stack)

                    if DEBUG:
                        print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
                        print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : postExp :", postExp)
                        print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)

                stack.append(ch)                                    
            
            else:
                push(stack, ch)
          
        else:
            postExp.append(ch)
        
        if DEBUG:
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : postExp :", postExp)
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)

    while not isEmpty(stack):
        postExp += pop(stack)

        if DEBUG:
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : postExp :", postExp)
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)

    return postExp

# This function evaluates the postfix expression.
def evalMod(inStr : str) -> str:

    if DEBUG:
        print()

    inExp = converterStringList(inStr)
    if DEBUG:
        print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : inExp :", inExp)
    postExp = converterPostExp(inExp)
    
    stack = []
    for ch in postExp:
        if not isOperator(ch):
            push(stack, ch)
        else:
            element2 = pop(stack)
            element1 = pop(stack)
            if ch == '+':
                intemediate_result = str(float(element1) + float(element2))
            elif ch == '-':
                intemediate_result = str(float(element1) - float(element2))
            elif ch == '*':
                intemediate_result = str(float(element1) * float(element2))
            elif ch == '/':
                    intemediate_result = str(float(element1) / float(element2))     # Zero division exception can occur. {to be handled}        
            push(stack, intemediate_result)

        if DEBUG:
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)
    
    result = pop(stack)     # Logical errors may arise in case of invalid input from the user.       

    return result

def processingTimeCalc(start_time : float, end_time : float) -> float:

    processingTime = end_time - start_time
    return processingTime

def main() -> None:
    print("\nWarning : Exceptions are not being handled.")
    if DEBUG:
        print("DEBUG : True")
    else:
        print("DEBUG : False")
    inStr = input("\nEnter a valid expression : ")          # Taking input from user.
    # print()
    start_time = time.time()
    result = evalMod(inStr)                                 # Calling the evalMod function
    
    if DEBUG:
        print("\nYOUR RESULT IS (CALCULATED BY ALGORITHM) : " + result)  
        print("True result (Calulated by in-build eval() function) :", eval(inStr))
    else:
        print("\nYOUR RESULT IS : " + result)

    end_time = time.time()

    print("\nProcessing time : ", processingTimeCalc(start_time, end_time), "seconds" '\n')

    return None

if __name__ == "__main__":
    main()                                                  # Calling main function
    