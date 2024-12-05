operators = {"+", "-", "*", "/", "//", "%", "<", ">", "<=", ">=", "=", "==", "**", "+=", "-=", "*=", "/=", "//="}

with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\data2.txt", "r") as f:
    data = f.read()

words = data.split()

operator_count = 0


for word in words:

    if(word in operators):
        operator_count += 1

    else:

        temp_word = ""

        i = 0
        while(i < len(word)):

            if(word[i] in operators):
                temp_word += word[i]
            
            elif(temp_word in operators):
                operator_count += 1
                temp_word = ""

            i += 1
        
        if(temp_word in operators):
            operator_count += 1

print(f"No. of operators are : {operator_count}")