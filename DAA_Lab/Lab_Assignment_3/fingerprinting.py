# Q13 :- Fingerprinting

class Fingerprinting:

    def __init__(self, str1 : str, str2 : str) -> None:
        self.str1 = str1
        self.str2 = str2

    def str_to_int(self, string : str):
        
        integer = ""
        for character in string:
            
            if(character.isdigit()):
                integer += character
            else:
                integer += str(ord(character))

        integer = int(integer)
        
        return integer

    def generate_prime_number(self):

        num : int = 2

        while(True):

            for divisor in range(2, num):

                if(num % divisor == 0):
                    break
            
            else:
                yield num

            num += 1 

    def compare(self) -> bool:
        
        self.str1 = self.str_to_int(self.str1)
        self.str2 = self.str_to_int(self.str2)

        prime_number_generator = self.generate_prime_number()

        for _ in range(100):
            
            next_prime_number = prime_number_generator.__next__()

            if(self.str1 % next_prime_number != self.str2 % next_prime_number):
                return False
            
        return True

    
def main() -> None:
    
    str1 : str = input("Enter string 1 : ")
    str2 : str = input("Enter string 2 : ")

    obj = Fingerprinting(str1, str2)
    comparison : bool = obj.compare()

    if(comparison):
        print("\nThe entered strings are identical.")
    else:
        print("\nThe entered strings are not identical.")


if(__name__ == "__main__"):
    print()
    main()
    print()
