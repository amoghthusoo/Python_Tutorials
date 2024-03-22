class Tries:

    def __init__(self):
        self.arr = []
        self.map_dict = {}

    def find_index_and_prefix(self, string : str):
        
        i = 0
        while(i < len(self.arr)):
            
            j = 0

            while(j < len(self.arr[i]) and j < len(string)):

                if(string[j] != self.arr[i][j]):
                    break
                    
                else:
                    j += 1

            if(j != 0):
                return i, j - 1
            
            i += 1

        return -1, -1
    
    def store_and_map(self, string : str) -> None:

        if(len(self.arr) == 0):
            self.arr.append(string)
        
        else:
            arr_index, str_index = self.find_index_and_prefix(string)
            
            if(arr_index == -1):
                self.arr.append(string)
            else:
                self.map_dict[len(self.arr)] = [arr_index, str_index]
                self.arr.append(string[(str_index + 1):])
    
    def regenerate_input(self):
        
        i = 0
        while(i < len(self.arr)):

            if(i not in self.map_dict):
                print(self.arr[i])
            else:
                arr_index = self.map_dict[i][0]
                str_index = self.map_dict[i][1]
                string = self.arr[arr_index][0:(str_index + 1)] + self.arr[i]
                print(string)
            i += 1


def main() -> None:
    
    obj = Tries()

    choice : str = "y"

    while(choice == "y"):
        word : str = input("Enter a word (without spaces): ")
        obj.store_and_map(word)

        choice = input("Do you want to add another word (y/n) : ")
    
    print("\nStored List : ", end="")
    print(obj.arr)
    print("Mapping Dictionery : ", end="")
    print(obj.map_dict)
    print("\nGenerated Output :\n")
    obj.regenerate_input()

if(__name__ == "__main__"):
    print()
    main()
    print()