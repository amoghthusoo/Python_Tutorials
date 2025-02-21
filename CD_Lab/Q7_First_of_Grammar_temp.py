print()

productions = ["S -> ABC", "A -> a|b|^", "B -> c|d|^", "C -> e|f|^"]
# productions = ["S -> Aa|b|^", "A -> D|a|^", "D -> S|d|^"]

production_enhanced_1 = []
for production in productions:
    production = production.replace(" ", "")
    split = production.split("->")
    production_enhanced_1.append([split[0], split[1]])

production_enhanced_2 = []

for production in production_enhanced_1:
    production_enhanced_2.append([production[0], production[1].split("|")])

productions = {}
for production in production_enhanced_2:
    productions[production[0]] = production[1]

print("Grammar : ")
for key, value in productions.items():
    print(f"{key} -> {value}")
print()


def calculate_first(non_terminal, first_set : set):
    
    for production in productions[non_terminal]:
        i = 0
        while(i < len(production)):

            if(production[i].islower() or production[i] == "^"):
                first_set.add(production[i])
                break

            else:
                temp = calculate_first(production[i], first_set)
                if("^" not in temp):
                    first_set.union(temp)
                    break
                
                else:    
                    if(i != len(production) - 1):
                        temp.remove("^")

                    first_set.union(temp)

            i += 1

    return first_set

print("First Sets : ")
for non_terminal in productions.keys():
    print(f"{non_terminal} : {sorted(list(calculate_first(non_terminal, set())))}")
            
print()