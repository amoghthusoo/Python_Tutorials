# Q3 :- Majority Element

class Majority_Element:

    def __init__(self):
        self.occurrence_dict = dict()

    def find_occurrence(self, arr):

        i = 0
        while(i < len(arr)):

            if(arr[i] not in self.occurrence_dict):
                self.occurrence_dict[arr[i]] = 1
            else:
                self.occurrence_dict[arr[i]] += 1
            i += 1

    def find_majority_element(self, arr : list) -> int | None:

        self.find_occurrence(arr)

        majority_element = arr[0]
        max_occurrence = self.occurrence_dict[arr[0]]

        for element, occurrence in self.occurrence_dict.items():
            
            if(occurrence > max_occurrence):
                max_occurrence = occurrence
                majority_element = element

        if(max_occurrence > len(arr)//2):
            return majority_element
        else:
            return None
        

def main():
    
    arr : str = input("Enter the array elements, separated by spaces : ")
    arr : list[int] = [int(e) for e in arr.split()]

    obj = Majority_Element()
    majority_element = obj.find_majority_element(arr)

    if(majority_element != None):
        print(f"\nThe majority element in the given array is : {majority_element}")
    else:
        print("\nMajority element NOT found.")

if(__name__ == "__main__"):
    print()
    main()
    print()
    