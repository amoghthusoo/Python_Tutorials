class OperatorCount:

    def __init__(self, path):
        self.path = path
        self.operators = {"+", "-", "*", "/", "%", "**", "//", 
                          "==", "!=", ">", "<", ">=", "<=",
                          "&", "|", "^", "~", "<<", ">>",
                          "=", "+=", "-=", "*=", "/=", "%=", "**=", "//=", "&=", "|=", "^=", ">>=", "<<=",
                          "and", "or", "not",
                          "is", "is not", "in", "not in"}
        self.found_operators = set()
        self.operator_count = 0
        self.temp_list = []

        try:
            with open(path, "r") as f:
                self.lines = f.readlines()
        except:
            print("Invalid Path!")
            print()
            quit()

        self.print_operator_count()

    def print_operator_count(self):
        
        for line in self.lines:
            words = line.rstrip("\n").split()
            
            i = 0
            while(i < len(words)):

                if(words[i] == "is"):

                    try:
                        if(words[i + 1] == "not"):
                            self.found_operators.add("is not")
                            self.operator_count += 1
                            self.temp_list.append("is not")
                            i += 2
                            continue

                        else:
                            self.found_operators.add("is")
                            self.operator_count += 1
                            self.temp_list.append("is")
                            i += 1
                            
                    except:
                        self.found_operators.add("is")
                        self.operator_count += 1
                        self.temp_list.append("is")
                        i += 1

                elif(words[i] == "not"):

                    try:
                        if(words[i + 1] == "in"):
                            self.found_operators.add("not in")
                            self.operator_count += 1
                            self.temp_list.append("not in")
                            i += 2
                            continue

                        else:
                            self.found_operators.add("not")
                            self.operator_count += 1
                            self.temp_list.append("not")
                            i += 1

                    except:
                        self.found_operators.add("not")
                        self.operator_count += 1
                        self.temp_list.append("not")
                        i += 1

                else:

                    if(words[i] in self.operators):
                        self.found_operators.add(words[i])
                        self.operator_count += 1
                        self.temp_list.append(words[i])
                        i += 1
                        continue

                    else:
                        temp_word = ""
                        j = 0
                        while(j < len(words[i])):
                            
                            if(words[i][j] in self.operators):
                                temp_word += words[i][j]
                            
                            elif(temp_word in self.operators):
                                self.found_operators.add(temp_word)
                                self.operator_count += 1
                                self.temp_list.append(temp_word)
                                temp_word = ""

                            j += 1
                        
                        if(temp_word in self.operators):
                            self.found_operators.add(temp_word)
                            self.operator_count += 1
                            self.temp_list.append(temp_word)


                        i += 1  

        # print(self.found_operators)
        # print(self.operator_count)
        # print(self.temp_list)

        print()
        print(f"Total number of operators : {self.operator_count}")
        print(f"Total number of distinct operators : {len(self.found_operators)}")
                              
            
def main():
    
    path = input("Enter the path of the file : ")
    obj = OperatorCount(path)

if(__name__ == "__main__"):
    print()
    main()
    print()