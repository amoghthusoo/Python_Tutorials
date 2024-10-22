from keyword import kwlist

class KeywordPrinting:

    def __init__(self, path):
        self.path = path
        self.keywords = set(kwlist)
        self.found_keywords = set()

        try:
            with open(path, "r") as f:
                self.lines = f.readlines()
        except:
            print("Invalid Path!")
            print()
            quit()

        self.print_keywords()

    def print_keywords(self):
        
        for line in self.lines:
            words = line.rstrip("\n").split()
            
            for word in words:

                temp_word = ""
                for ch in word:
                    if(ch.isalpha()):
                        temp_word += ch

                word = temp_word

                if(word in self.keywords):
                    self.found_keywords.add(word)
                    continue

                i = 0    
                temp_word = ""
                while(i < len(word)):
                    
                    temp_word += word[i]
                    if(temp_word in self.keywords):
                        self.found_keywords.add(temp_word)
                        break

                    i += 1

        print()
        print("Distinct Keywords : ")
        for i, keyword in enumerate(self.found_keywords):
            print(f"{i + 1}. {keyword}")

def main():
    
    path = input("Enter the path of the file : ")
    obj = KeywordPrinting(path)

if(__name__ == "__main__"):
    print()
    main()
    print()