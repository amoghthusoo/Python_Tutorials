path = input("Path : ")
with open(path, "r") as f:
    lines = f.readlines()

i = 0
while(i < len(lines)):
    lines[i] = lines[i].rstrip()
    i += 1

operators = {"+", "-", "*", "/", "//", "%", "=", "==", "+=", "-=", "*=", "/=", "//="}
found_operators = set()
for line in lines:

    words = line.split()

    for word in words:

        if(word in operators):
            found_operators.add(word)
            continue

        
        i = 0
        temp_word = ""

        while(i < len(word)):
            
            if(word[i] in operators):
                temp_word += word[i]
            
            else:
                
                if(temp_word in operators):
                    found_operators.add(temp_word)
                
                temp_word = ""
            
            i += 1

print(found_operators)
        