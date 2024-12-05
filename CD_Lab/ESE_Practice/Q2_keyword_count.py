from keyword import kwlist

keywords = set(kwlist)

with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\data.txt", "r") as f:
    data = f.read()

words = data.split()

keyword_count = 0

for word in words:

    if(word in keywords):
        keyword_count += 1

    else:
        temp_word = ""

        i = 0
        while(i < len(word)):
            temp_word += word[i]

            if(temp_word in keywords):
                keyword_count += 1
                break

            i += 1

print(f"Total no. of keywords are : {keyword_count}")
