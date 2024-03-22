# Q8 :- Master Method

import math

class Master_Method:
    
    def __init__(self, relation : str) -> None:
        
        self.a = int(relation[5])
        self.b = int(relation[11])
        self.k = int(relation[16])

    def check_regularity_condition(self):
        
        c : float = self.a / (self.b ** self.k)
        if(c < 1):
            return True
        else:
            return False

    def calculate_complexity(self) -> str | None:
        
        left_quantity : float = math.log(self.a, self.b)

        if(left_quantity > self.k):
            return f"Theta(n^{round(left_quantity, 2)})"
        
        elif(self.k > left_quantity):

            if(self.check_regularity_condition()):
                return f"Theta(n^{round(self.k, 2)})"
            else:
                print("\nMaster Method cannot be applied.")
                return None
        
        elif(left_quantity == self.k):
            
            print("\nMaster Method cannot be applied.")
            return None


def remove_spaces(relation : str) -> str:

    return relation.replace(" ", "")

def is_valid(relation : str) -> bool:
    
    if (
        relation[0:5] == "T(n)=" and
        relation[6:11] == "*T(n/" and 
        relation[12:16] == ")+n^" and 
        relation[17:24] == "*log(n)" and 

        relation[5].isdigit() and
        relation[11].isdigit() and
        relation[16].isdigit()
        ):

        if(int(relation[16]) >= 4):
            return False
        else:
            return True
    else:
        return False

def main():
    # T(n)=a*T(n/b)+n^k*log(n)

    print("T(n) = a * T(n/b) + n^k * log(n)")
    relation : str = input("Enter the relation in the above format : ")

    relation = remove_spaces(relation)

    if(is_valid(relation)):
        
        obj : Master_Method = Master_Method(relation)
        complexity : str = obj.calculate_complexity()

        if(complexity != None):
            print(f"\nThe time complexity for the relation is given by : {complexity}")
    
    else:
        print("\nINVALID INPUT!")


if(__name__ == "__main__"):
    print()
    main()
    print()
