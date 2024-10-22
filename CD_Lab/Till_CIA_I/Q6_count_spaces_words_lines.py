class CharacterSpacesWordsLines:

    def __init__(self, path):
        self.path = path
        self.occr_dict = {}

        self.blank_count = 0
        self.line_count = 0
        self.word_count = 0
        
        try:
            with open(path, "r") as f:
                self.lines = f.readlines()
        except:
            print("Invalid Path!")
            print()
            quit()

        self.count_spaces_words_lines()

    def count_spaces_words_lines(self):
        
        self.line_count = len(self.lines)

        for line in self.lines:
            for ch in line:
                if(ch == " "):
                    self.blank_count += 1

            self.word_count += len(line.split())

        print()
        print(f"Total number of blank spaces : {self.blank_count}")
        print(f"Total number of words : {self.word_count}")
        print(f"Total number of lines : {self.line_count}")
        
def main():
    
    path = input("Enter the path of the file : ")
    obj = CharacterSpacesWordsLines(path)

if(__name__ == "__main__"):
    print()
    main()
    print()