class CharacterOccurrence:

    def __init__(self, path):
        self.path = path
        self.occr_dict = {}

        try:
            with open(path, "r") as f:
                self.lines = f.readlines()
        except:
            print("Invalid Path!")
            print()
            quit()

        self.print_character_occurrence()

    def print_character_occurrence(self):
        
        for line in self.lines:
            line = line.rstrip("\n")
            
            for ch in line:
                
                if(ch not in [" "]):
                    if(ch not in self.occr_dict):
                        self.occr_dict[ch] = 1
                    else:
                        self.occr_dict[ch] += 1

        i = 1
        print()
        print("Character Occurrences : ")
        for ch, occr in self.occr_dict.items():
            print(f"{i}. {ch} -> {occr}")
            i += 1

def main():
    
    path = input("Enter the path of the file : ")
    obj = CharacterOccurrence(path)

if(__name__ == "__main__"):
    print()
    main()
    print()