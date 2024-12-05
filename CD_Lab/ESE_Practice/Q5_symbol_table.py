class SymbolTable:

    def __init__(self):
        self.table = dict()

    def add(self, name, type, size):

        if(name not in self.table):
            self.table[name] = [type, size]
        
        else:
            print("Symbol already exists!")

    def delete(self, name):

        if(name not in self.table):
            print("Symbol doesn't exist!")
        
        else:
            self.table.pop(name)

    
    def display(self):
        print("Name -> [Type, Size]")
        for key, val in self.table.items():
            print(f"{key} -> {val}")

table = SymbolTable()
table.add("x", "int", 4)
table.add("ch", "char", 1)
table.add("arr", "int[]", 12)
table.delete("y")
table.display()
