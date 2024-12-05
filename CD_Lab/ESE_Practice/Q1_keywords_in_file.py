from keyword import kwlist

keywords = set(kwlist)

with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\Q2.txt", "r") as f:
    data = f.read()

words = data.split()

found_keywords = set()

for word in words:

    if(word in keywords):
        found_keywords.add(word)

    else:
        temp_word = ""

        i = 0
        while(i < len(word)):
            temp_word += word[i]

            if(temp_word in keywords):
                found_keywords.add(temp_word)
                break

            i += 1

print("Found keywords: ")
for keyword in found_keywords:
    print(keyword)
