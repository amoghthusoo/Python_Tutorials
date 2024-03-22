class Solution:

    def print_pattern(self, n):
    
        print(n, end = " ")

        if(n <= 0):
            return
        else:
            self.print_pattern(n - 5)

        print(n, end = " ")

def main():
    
    n : int = int(input("Enter the value of n : "))
    obj = Solution()
    print()
    obj.print_pattern(n)

if(__name__ == "__main__"):
    print()
    main()
    print("\n")
    