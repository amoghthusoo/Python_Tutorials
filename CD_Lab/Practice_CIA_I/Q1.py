from keyword import kwlist
path = input("Path : ")
with open(path, "r") as f:
    lines = f.readlines()
i = 0
while(i < len(lines)):
    lines[i] = lines[i].rstrip("\n")
    i += 1
keywords = set(kwlist)
found_keywords = set()
for line in lines:
    words = line.split()

    for word in words:

        if(word in keywords):
            found_keywords.add(word)
            continue
        
        temp_word = ""
        i = 0
        while(i < len(word)):
            temp_word += word[i]
            if(temp_word in keywords):
                found_keywords.add(temp_word)
                break
            i += 1
for keyword in found_keywords:
    print(keyword)