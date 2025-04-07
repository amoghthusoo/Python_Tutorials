class CustomAdder:

    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y

    def add(self) -> int:

        result = self.x + self.y

        if(15 < result < 20):
            return 20
        else:
            return result
        
def main() -> None:

    x = int(input("\nEnter first integer : "))
    y = int(input("Enter second integer : "))

    obj = CustomAdder(x, y)

    result = obj.add()

    print(f"\nThe required result for the given inputs is : {result}\n")

if(__name__ == "__main__"):
    main()
