class FirstSet:

    def __init__(self, productions):
        self.productions = productions

    def print_first_sets(self):
        
        production_enhanced_1 = []
        
        for production in self.productions:
            production = production.replace(" ", "")
            split = production.split("->")
            production_enhanced_1.append([split[0], split[1]])

        production_enhanced_2 = []

        for production in production_enhanced_1:
            production_enhanced_2.append([production[0], production[1].split("|")])

        self.productions = {}
        for production in production_enhanced_2:
            self.productions[production[0]] = production[1]

        print("Grammar : ")
        for key, value in self.productions.items():
            print(f"{key} -> ", end="")
            i = 0
            while(i < len(value)):
                print(value[i], end="")
                if(i != len(value) - 1):
                    print(" | ", end="")
                i += 1
            print()
        print()

        print("First Sets : ")
        for non_terminal in self.productions.keys():
            first_set = sorted(list(self.calculate_first(non_terminal, set())))
            print(f"{non_terminal} : ", end = "")
            print("{", end="")
            i = 0
            while(i < len(first_set)):
                print(first_set[i], end="")
                if(i != len(first_set) - 1):
                    print(", ", end="")
                i += 1
            print("}")
    
    def calculate_first(self, non_terminal, first_set : set):
    
        for production in self.productions[non_terminal]:
            i = 0
            while(i < len(production)):

                if(production[i].islower() or production[i] in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-", "/"]):
                    if(production[i] == "i"):
                        try:
                            if(production[i + 1] == "d"):
                                first_set.add("id")
                                break
                        except:
                            pass
                            
                    first_set.add(production[i])
                    break

                else:
                    temp = self.calculate_first(production[i], first_set)
                    if("^" not in temp):
                        first_set.union(temp)
                        break
                    
                    else:    
                        if(i != len(production) - 1):
                            temp.remove("^")

                        first_set.union(temp)

                i += 1

        return first_set

def main():
    
    # productions = ["S -> ABC", "A -> a|b|^", "B -> c|d|^", "C -> e|f|^"]
    productions = ["E -> TX", "X -> *TX|^", "T -> FY", "Y -> +FY|^", "F -> id|(E"]
    obj = FirstSet(productions)
    obj.print_first_sets()

if(__name__ == "__main__"):
    print()
    main()
    print()
