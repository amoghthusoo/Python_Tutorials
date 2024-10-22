from copy import deepcopy
from math import pow

class Matrix_Chain_Multiplication:

    def __init__(self, p : list[int]) -> None:
        
        self.INF = int(pow(2, 31))

        self.p : list[int] = p
        self.m : list[list[int]] = [[None for _ in range(len(p) - 1)] for _ in range(len(p) - 1)]
        self.s : list[list[int]] = deepcopy(self.m) 
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

        d : int = 1
        while(d < len(self.m)):

            j : int = d
            i : int = 0
            while(i < len(self.m) - d):

                
                k : int = i
                while(k < j):

                    temp = self.m[i][k] + self.m[k + 1][j] + self.p[i] * self.p[k + 1] * self.p[j + 1]
                    
                    if(temp < self.m[i][j]):
                        self.m[i][j] = temp
                        self.s[i][j] = k + 1


                    k += 1

                i += 1
                j += 1            

            d += 1
        
def main() -> None:
    
    p = [12, 6, 8, 15, 7]
    obj = Matrix_Chain_Multiplication(p)
    obj.construct()
    
    for e in obj.m:
        print(e)
    print()
    for e in obj.s:
        print(e)



if(__name__ == "__main__"):
    print()
    main()
    print()