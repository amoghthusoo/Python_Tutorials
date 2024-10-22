from keyword import kwlist

class KeywordCount:

    def __init__(self, path):
        self.path = path
        self.keywords = set(kwlist)
        self.found_keywords = set()
        self.keyword_count = 0

        try:
            with open(path, "r") as f:
                self.lines = f.readlines()
        except:
            print("Invalid Path!")
            print()
            quit()

        self.print_keyword_count()

    def print_keyword_count(self):
        
        for line in self.lines:
            words = line.rstrip("\n").split()
            
            for word in words:

                if(word in self.keywords):
                    self.found_keywords.add(word)
                    self.keyword_count += 1
                    break
                
                i = 0    
                temp_word = ""
                while(i < len(word)):
                    
                    temp_word += word[i]
                    if(temp_word in self.keywords):
                        self.found_keywords.add(temp_word)
                        self.keyword_count += 1
                        break

                    i += 1

        print()
        print(f"Total number of keywords : {self.keyword_count}")
        print(f"Total number of distinct keywords : {len(self.found_keywords)}")


def main():
    
    path = input("Enter the path of the file : ")
    obj = KeywordCount(path)

if(__name__ == "__main__"):
    print()
    main()
    print()