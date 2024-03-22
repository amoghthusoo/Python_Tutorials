# eval() implementation in python.
# NOTE :- The program cannot handle any exceptions as of now.
# WARNING :- DEBUG can increase the processing time, meant for debugging purpose only.

import time
DEBUG : bool = True            # DEBUG can be set to True or False.

class Evaluate:
    # <---------------------------------Implementation of Stacks starts here----------------------------------------->

    # push function for stack implementation
    def push(self, stack : list, element : str) -> None:
        
        stack.append(element)
        return None

    # pop function for stack implementation
    def pop(self, stack : list) -> str:
        
        if (len(stack) == 0):
            if (DEBUG):
                print("\nDEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : OUT : Underflow")
            return None
        else:
            return stack.pop()
        
    # isEmpty function for stack implementation
    def isEmpty(self, stack : list) -> bool:
        
        if (len(stack) == 0):
            if (DEBUG):
                print("\nDEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : OUT : Stack is empty!")
            return True
        else:
            return False

    # top function for stack implementation
    def top(self, stack : list) -> None | str:
        
        if (self.isEmpty(stack)):
            return None
        else:
            return stack[-1]

    # size function for stack implementation
    def size(self, stack : list) -> int:
        return len(stack)

    # <---------------------------------Implementation of Stacks ends here----------------------------------------->

    # This returns the relative precedence of arithmetic operators
    def precedence(self, operator : str) -> int:

        if operator in ['(', ')']:
            return -1                                   # Do not confuse with the actual precedence of brackets. {Added during debugging process.}
        elif operator in ['+', '-']:
            return 0
        elif operator in ['*', '/']:
            return 1

    # This function returns whether the character is an operator or not    
    def isOperator(self, character : str) -> bool:
        
        if character in ['+', '-', '*', '/', '(', ')']:             # '(' and ')' are added to the list during debugging process.         
            return True
        else:
            return False

    # This function converts the input expression which is stored in a string into the list.
    """
    It is found that processing the input expression directly; only works with single digit numbers.
    After this conversion, processing the inExp works for double digts as well and so on.
    """ 
    def converterStringList(self, inStr : str) -> list:

        if (DEBUG):
            print()

        inExp : list = []
        inStr_index : int = 0
        inExp_index : int = 0
        unary_memory : bool = True                      # Counter for the total number of indices in "inExp" list.                                   
        while (inStr_index < len(inStr)):               #{Added during debugging, handles the case when expression starts with unary operator}
            if (not self.isOperator(inStr[inStr_index])):
                
                if (inStr_index == 0):
                    inExp.append(inStr[inStr_index])
                
                elif (inStr_index > 0) and (self.isOperator(inExp[0][0])) and (unary_memory): # {Added during debugging, handles the case when expression starts with unary operator}
                    inExp[inExp_index] += inStr[inStr_index]                                  # <--------------------------------------do------------------------------------------->

                elif (self.isOperator(inExp[-1])):
                    inExp.append(inStr[inStr_index])
                    inExp_index += 1
                
                else:
                    inExp[inExp_index] += inStr[inStr_index]
            
            elif (self.isOperator(inStr[inStr_index])):
                inExp.append(inStr[inStr_index])
                
                if (inStr_index != 0):      # {Added during debugging, handles the case when expression starts with unary operator}
                    inExp_index += 1

                if (inExp_index == 1):      # {Added during debugging, handles the case when expression starts with unary operator}
                    unary_memory = False    # <--------------------------------------do------------------------------------------->
                
            inStr_index += 1

            if (DEBUG):
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : inExp :", inExp)

        return inExp

    # This function converts the infix expression to postfix expression.
    def converterPostExp(self, inExp : list) -> list:

        if (DEBUG):
            print()

        postExp : list = []
        stack : list = []

        for ch in inExp:

            if ch == '(':
                self.push(stack, ch)

            elif ch == ')':
                
                while True:
                    popped_character : str = self.pop(stack)
                    if popped_character == '(':
                        break
                    else:
                        postExp.append(popped_character)

            elif self.isOperator(ch):

                if self.isEmpty(stack):
                    self.push(stack, ch)

                elif (self.precedence(ch) <= self.precedence(self.top(stack))):            # Equality handles the associativity of operators from left to right

                    while (not self.isEmpty(stack)):

                        top_character : str = self.top(stack)

                        if (self.precedence(top_character) < self.precedence(ch)):
                            break
                        
                        else:
                            postExp += self.pop(stack)

                        if (DEBUG):
                            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
                            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : postExp :", postExp)
                            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)

                    stack.append(ch)                                    
                
                else:
                    self.push(stack, ch)
            
            else:
                postExp.append(ch)
            
            if (DEBUG):
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : postExp :", postExp)
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)

        while (not self.isEmpty(stack)):
            postExp += self.pop(stack)

            if (DEBUG):
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : postExp :", postExp)
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)

        return postExp

    # This function evaluates the postfix expression.
    def evalMod(self, inStr : str) -> str:

        if (DEBUG):
            print()

        inExp = self.converterStringList(inStr)
        if (DEBUG):
            print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : inExp :", inExp)
        postExp = self.converterPostExp(inExp)
        
        stack : list = []
        for ch in postExp:
            if (not self.isOperator(ch)):
                self.push(stack, ch)
            else:
                element2 : str = self.pop(stack)
                element1 : str = self.pop(stack)
                if (ch == '+'):
                    intemediate_result : str = str(float(element1) + float(element2))
                elif (ch == '-'):
                    intemediate_result : str = str(float(element1) - float(element2))
                elif (ch == '*'):
                    intemediate_result : str = str(float(element1) * float(element2))
                elif (ch == '/'):
                        intemediate_result : str = str(float(element1) / float(element2))  # Zero division exception can occur. {to be handled}        
                self.push(stack, intemediate_result)

            if (DEBUG):
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : ch :", ch)
                print("DEBUG : " + time.strftime("%d %b %Y %H:%M:%S") + " : stack :", stack)
        
        result : str = self.pop(stack)     # Logical errors may arise in case of invalid input from the user.       

        return result

    def processingTimeCalc(self, start_time : float, end_time : float) -> float:

        processingTime : float = end_time - start_time
        return processingTime

def main() -> None:
    print("\nWarning : Exceptions are not being handled.")
    if (DEBUG):
        print("DEBUG : True")
    else:
        print("DEBUG : False")
    inStr : str = input("\nEnter a valid expression : ")          # Taking input from user.
    # print()
    start_time : float = time.time()
    obj = Evaluate()
    result : str = obj.evalMod(inStr)                                 # Calling the evalMod function
    
    if (DEBUG):
        print()
        for i in range(1, 48 + len(result)):
            print("-", end = "")
        print("\n| YOUR RESULT IS (CALCULATED BY ALGORITHM) : " + result + " |")
        for i in range(1, 48 + len(result)):
            print("-", end = "")
        print("\nTrue result (Calulated by in-build eval() function) :", eval(inStr))
    else:
        for i in range(1, 22 + len(result)):
            print("-", end = "")
        print("\n| YOUR RESULT IS : " + result + " |")
        for i in range(1, 22 + len(result)):
            print("-", end = "")

    end_time : float = time.time()

    print("\nProcessing time : ", obj.processingTimeCalc(start_time, end_time), "seconds" '\n')

    return None

if __name__ == "__main__":
    main()                                                  # Calling main function
    