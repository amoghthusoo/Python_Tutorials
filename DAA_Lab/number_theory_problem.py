class Solution:

    def __init__(self, a : int, b : int, c : int) -> None:
        self.a = a
        self.b = b
        self.c = c


    def pow(self, base : int, exponent : int) -> int:
        
        result : int = base

        for i in range(exponent - 1):
            result = (result * base) % 10

        return result

    def calculate(self) -> int:
        
        beta : int = self.pow(self.b, self.c)

        if(beta == 0):
            return 0
        elif(beta == 1):
            return (self.a % 10)
        else:
            return self.pow(self.a, beta)
        
class Main:

    def __init__(self) -> None:
        pass

    def main(self):

        a : int = 1943
        b : int = 1645
        c : int = 1053

        solution_obj : Solution = Solution(a, b, c)
        result : int = solution_obj.calculate()
        print(result)


if(__name__ == "__main__"):
    obj : Main = Main()
    obj.main()
