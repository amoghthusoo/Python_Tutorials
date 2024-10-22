path = input("Path : ")
with open(path, "r") as f:
    lines = f.readlines()
line_count = len(lines)
space_count = 0
word_count = 0
for line in lines:

    for ch in line:
        if(ch == " "):
            space_count += 1
    
    word_count += len(line.split())

print(f"Line Count : {line_count}")
print(f"Space Count : {space_count}")
print(f"Word Count : {word_count}")
