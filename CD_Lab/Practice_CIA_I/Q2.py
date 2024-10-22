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
total_count = 0
for line in lines:
    words = line.split()

    for word in words:

        if(word in keywords):
            found_keywords.add(word)
            total_count += 1
            continue
        
        temp_word = ""
        i = 0
        while(i < len(word)):
            temp_word += word[i]
            if(temp_word in keywords):
                found_keywords.add(temp_word)
                total_count += 1
                break
            i += 1
print(f"Total keywords = {total_count}")
print(f"Unique keywords = {len(found_keywords)}")