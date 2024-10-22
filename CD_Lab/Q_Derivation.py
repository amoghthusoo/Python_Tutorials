class Derivation:

    def __init__(self):
        self.grammar = ["aSa", "bSb", "aa", "bb"]

    def analyze(self, input_str):
        self.find_used_productions(input_str)

    def find_used_productions(self, input_str):
        
        used_productions = []

        half_index = (len(input_str) // 2) - 1

        i = 0
        while(i <= half_index):
            
            if(input_str[i] == "a"):
                
                if(i != half_index):
                    used_productions.append(self.grammar[0])
                else:
                    used_productions.append(self.grammar[2])

            elif(input_str[i] == "b"):

                if(i != half_index):
                    used_productions.append(self.grammar[1])
                else:
                    used_productions.append(self.grammar[3])
            
            i += 1

        self.generate_derivation(used_productions, input_str)

    def generate_derivation(self, used_productions, input_str):
        
        derivation = []
        derivation.append(used_productions[0])
        
        i = 1
        while(i < len(used_productions)):
            derivation.append(derivation[-1].replace("S", used_productions[i]))
            i += 1

        if(derivation[-1] == input_str):
            self.print_derivation(derivation)
        else:
            print("Can't create a derivation.")

    def print_derivation(self, derivation):

        print("Derivation :")
        print("S -> ", end="")
        i = 0
        while(i < len(derivation)):

            print(derivation[i], end="")

            if(i != len(derivation) - 1):
                print(" -> ", end="")
            else:
                print()

            i += 1

def main():
    obj = Derivation()
    while(True):
        input_str = input("Enter input string : ")
        obj.analyze(input_str)
        print()

if(__name__ == "__main__"):
    main()