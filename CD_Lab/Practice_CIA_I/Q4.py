path = input("Path : ")
with open(path, "r") as f:
    lines = f.readlines()
i = 0
while(i < len(lines)):
    lines[i] = lines[i].rstrip("\n")
    i += 1

occr_dict = {}
for line in lines:
    for ch in line:
        if(ch not in occr_dict):
            occr_dict[ch] = 1
        else:
            occr_dict[ch] += 1    

occr_dict.pop(" ")
for ch, occr in occr_dict.items():
    print(f"{ch} -> {occr}")