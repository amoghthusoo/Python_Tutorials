# Q1 :- Asymptotic Growth

import math

class Function:

    def __init__(self, function : str, name : str,  value : int | float) -> None:
        self.function : str = function
        self.name : str = name
        self.value : int | float =  value

class Asymptotic_Growth:

    def f1(self, n : int) -> int:
        return 10 ** n

    def f2(self, n : int) -> int:
        return math.factorial(n)

    def f3(self, n : int) -> float:
        return n ** (n ** 0.5)

    def f4(self, n : int) -> float:
        return 2 ** math.log2(n)
    
    def f5(self, n : int) -> float:
        return n ** (math.log2(n))
    
    def print_horizontal_line(self, n):

        for i in range(n):
            print("-", end="")

        print()
    
    def display_function(self):
        
        self.print_horizontal_line(47)

        print("| Given Functions :                           |")
        print("|                                             |")
        print("| f1 = 10^n                                   |")
        print("| f2 = n!                                     |")
        print("| f3 = n^(n^0.5)                              |")
        print("| f4 = 2^log(n)                               |")
        print("| f5 = n^log(n)                               |")

        self.print_horizontal_line(47)
    
    def sort(self, comparison_list : list[Function]) -> None:
        
        i = 0
        while(i < len(comparison_list) - 1):

            j = 0
            while(j < len(comparison_list) - 1 - i):

                if(comparison_list[j].value > comparison_list[j + 1].value):
                    comparison_list[j], comparison_list[j + 1] = comparison_list[j + 1], comparison_list[j]

                j += 1
            i += 1

    def display_comparison_list(self, comparison_list : list[Function]):
        
        print("| Asymptotic Growth Rate :                    |")
        print("|                                             |")
        print("| ", end="")
        i = 0
        while(i < len(comparison_list)):

            print(comparison_list[i].name, end="")

            if(i != len(comparison_list) - 1):
                print(" < ", end="")
            else:
                print(" |")

            i += 1

        print("| ", end="")
        i = 0
        while(i < len(comparison_list)):

            print(comparison_list[i].function, end="")

            if(i != len(comparison_list) - 1):
                print(" < ", end="")
            else:
                print("                      |")

            i += 1

        self.print_horizontal_line(47)


    def calculate_asymptotic_growth(self, n : int):
        
        comparison_list : list = []

        comparison_list.append(Function("f1", "10^n", self.f1(n)))
        comparison_list.append(Function("f2", "n!", self.f2(n)))
        comparison_list.append(Function("f3", "n^(n^0.5)", self.f3(n)))
        comparison_list.append(Function("f4", "2^log(n)", self.f4(n)))
        comparison_list.append(Function("f5", "n^log(n)", self.f5(n)))

        self.sort(comparison_list)

        return comparison_list

def main():
    
    n = 100
    ob = Asymptotic_Growth()
    result = ob.calculate_asymptotic_growth(n)
    ob.display_function()
    ob.display_comparison_list(result)

if(__name__ == "__main__"):
    print()
    main()
    print()
    