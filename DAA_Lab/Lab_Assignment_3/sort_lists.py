# Q14 :- Sort Lists

class Sort_Lists:

    def sort_lists(self, lists : list[list[int]]) -> list[int]:

        sorted_list = []

        while(True):

            i : int = 0
            min_element_list_index = 0
            while(i < len(lists)):

                # try:
                if(lists[i][0] < lists[min_element_list_index][0]):
                    min_element_list_index = i
                # except:
                #     lists.pop(i)
                
                i += 1

            if(len(lists) == 0):
                break

            sorted_list.append(lists[min_element_list_index].pop(0))
            if(len(lists[min_element_list_index]) == 0):
                lists.pop(min_element_list_index)

        return sorted_list            

def main() -> None:
    
    lists = []
    choice : str = "y"
    while(choice == "y"):
        
        _list = input("Enter the elements of the list in sorted order, separated by spaces : ")
        lists.append([int(e) for e in _list.split()])

        choice = input("Do you want to enter another list (y/n) : ")
        print()

    # lists = [
    #     [1, 8],
    #     [3, 4, 11, 15],
    #     [6, 20, 30]
    # ]

    obj = Sort_Lists()
    sorted_list = obj.sort_lists(lists)
    print("\nSorted List : ")
    print(sorted_list)


if(__name__ == "__main__"):
    print()
    main()
    print()
    