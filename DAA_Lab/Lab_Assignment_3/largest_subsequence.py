# Q9 :- Largest Common Subsequence

class Largerst_Sub_Sequence:

    def get_subsequences(self, string : str) -> list[str]:
        
        bin_num_list = [bin(num)[2:].zfill(len(string)) for num in range(1, int(2 ** len(string)) )]

        subsequences = []

        for bin_num in bin_num_list:

            temp_str = ""
            for i in range(len(bin_num)):
                
                if(bin_num[i] == "1"):
                    temp_str += string[i]
                
            subsequences.append(temp_str)

        return subsequences

    def find_largest_common_sub_sequence(self, str1 : str, str2 : str) -> str:

        str1_subsequences = self.get_subsequences(str1)    
        str2_subsequences = self.get_subsequences(str2)    

        largest_subsequence = ""

        for word in str1_subsequences:

            if(word in str2_subsequences):

                if(len(word) > len(largest_subsequence)):
                    largest_subsequence = word

        return largest_subsequence
        
    
def main() -> None:

    str1 = input("Enter the first string : ")
    str2 = input("Enter the second string : ")

    obj = Largerst_Sub_Sequence()
    largest_commone_sub_sequence = obj.find_largest_common_sub_sequence(str1, str2)

    if(largest_commone_sub_sequence):
        print(f"\nLargest commone sub sequence for the given strings is : {largest_commone_sub_sequence}")
    else:
        print("\nNo common subsequence found!")
    

if(__name__ == "__main__"):
    print()
    main()
    print()
