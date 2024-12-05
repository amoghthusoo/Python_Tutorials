with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\data.txt", "r") as f:
    data = f.read()

words = data.split()

occr_dict = {}

for word in words:

    for ch in word:

        if(ch not in occr_dict):
            occr_dict[ch] = 1
        else:
            occr_dict[ch] += 1

print("Occurrence of each character : ")
for ch, occr in occr_dict.items():
    print(f"{ch} -> {occr}") 