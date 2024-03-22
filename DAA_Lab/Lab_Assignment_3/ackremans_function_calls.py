# Q12 :- Ackreman's Function Calls

import sys
import math
sys.setrecursionlimit(int(math.pow(10, 7)))

class Ackreman_Function_Calls:

    def __init__(self) -> None:
        self.total_calls = 0

    def calculate_ackreman_function_calls(self, m : int, n : int) -> int:
        result : int = self.ackreman_function(m, n)
        return self.total_calls
    
    def ackreman_function(self, m : int, n : int) -> int:
        
        self.total_calls += 1
        # print(self.total_calls)

        if(m == 0):
            return n + 1
        
        elif(m > 0 and n == 0):
            return self.ackreman_function(m - 1, 1)
        
        elif(m > 0 and n > 0):
            return self.ackreman_function(m - 1, self.ackreman_function(m, n - 1))

def main():
    
    m : int = int(input("Enter the value of m : "))
    n  : int = int(input("Enter the value of n : "))
    
    obj = Ackreman_Function_Calls()
    total_calls = obj.calculate_ackreman_function_calls(m, n)

    print(f"\nTotal number of function calls of Ackeraman Function is : {total_calls}")
    

if(__name__ == "__main__"):
    print()
    main()
    print()
