grammer = ["S -> ABC", "A -> a|b|^", "B -> c|d|^", "C -> e|f|^"]

productions = {}

for e in grammer:
    e = e.replace(" ", "")
    temp = e.split("->")
    l = temp[0]
    r = temp[1].split("|")
    productions[l] = r

def find_first(non_terminal, first_set : set):

    for p in productions[non_terminal]:

        i = 0
        while(i < len(p)):

            if(p[i].islower() or p[i] == "^"):
                first_set.add(p[i])
                break
                
            else:
                temp = find_first(p[i], first_set)
                if("^" not in temp):
                    first_set.union(temp)
                    break
                else:
                    if(i != len(p) - 1):
                        temp.remove("^")
                    
                    first_set.union(temp)
            
            i += 1
    
    return first_set

for key in productions.keys():
    print(f"{key} : {find_first(key, set())}")