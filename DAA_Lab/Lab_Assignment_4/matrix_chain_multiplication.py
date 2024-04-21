# Q2 :- Matrix Chain Multiplication

from copy import deepcopy
from math import pow

class Matrix_Chain_Multiplication:

    def __init__(self, p : list[int]) -> None:
        
        self.INF = int(pow(2, 31))

        self.p : list[int] = p
        
        self.m : list[list[int]] = [[None for _ in range(len(p) - 1)] for _ in range(len(p) - 1)]
        self.s : list[list[int]] = deepcopy(self.m) 
        
        self.a = [i for i in range(1, len(p))]

        self.initialise()


    def initialise(self) -> None:
        
        i : int = 0
        while(i < len(self.m)):

            j : int = 0
            while(j < len(self.m)):

                if(i == j):
                    self.m[i][j] = 0
                
                elif(i < j):
                    self.m[i][j] = self.INF
                    self.s[i][j] = self.INF

                j += 1
            i += 1

    def construct(self) -> None:

        d = 1
        while(d < len(self.m)):

            j = d
            i = 0
            while(i < len(self.m) - d):

                
                k = i
                while(k < j):

                    temp = self.m[i][k] + self.m[k + 1][j] + self.p[i] * self.p[k + 1] * self.p[j + 1]
                    
                    if(temp < self.m[i][j]):
                        self.m[i][j] = temp
                        self.s[i][j] = k + 1

                    k += 1

                i += 1
                j += 1            

            d += 1

    def insert_brackets(self, lower_bound, upper_bound):
        self.a.insert(self.a.index(lower_bound), "(")
        self.a.insert(self.a.index(upper_bound) + 1, ")")

    def find_partition(self, lower_bound, upper_bound):
        
        if(upper_bound - lower_bound + 1 <= 2):
            return

        partition = self.s[lower_bound - 1][upper_bound - 1]
        
        if(partition - lower_bound + 1 >= 2):
            self.insert_brackets(lower_bound, partition)

        if(upper_bound - partition >= 2):
            self.insert_brackets(partition + 1, upper_bound)

        self.find_partition(lower_bound, partition)
        self.find_partition(partition + 1, upper_bound)
    
    def construct_result_string(self):
        
        self.a.insert(0, "(")
        self.a.append(")") 

        out_string = ""
        
        for element in self.a:
            if(element not in ["(", ")"]):
                out_string += "A" + str(element)
            else:
                out_string += element

        return out_string
    
    def get_result(self):
        self.construct()
        self.find_partition(1, len(self.p) - 1)
        return self.construct_result_string()
        
def main() -> None:
    
    p = input("Enter the element of p array, separated by spaces : ")
    p = [int(e) for e in p.split()]

    obj = Matrix_Chain_Multiplication(p)
    out = obj.get_result()
    print("\nOptimal Parenthesization : " + out)
    
    # print(obj.m)
    # print(obj.s)
    

if(__name__ == "__main__"):
    print()
    main()
    print()
