class Table:

    def __init__(self, *attributes):
        
        self.attr_length = len(attributes)
        self.attributes_index = {}

        for index, attr in enumerate(attributes):
            self.attributes_index[index] = attr

        self.table = dict()

    def insert(self, *attributes):
        
        if(len(attributes) != self.attr_length):
            print("Arguments Mismatch")
            return
        
        if(self.exists(attributes[0])):
            print("Entry already exists!")
            return
        
        self.table[attributes[0]] = list(attributes[1:])
        

    def delete(self, target):
        
        if(not self.exists(target)):
            print("Entry not found!")
            return
        
        self.table.pop(target)

    def exists(self, target):

        if(target in self.table):
            return True
        else:
            return False
    
    def get_keys(self):
        return list(self.table.keys())
    
    def get_value(self, key):
        
        if(not self.exists(key)):
            print("Entry not found!")
        else:
            return self.table[key]
    
    def get_attributes(self):
        return list(self.attributes_index.values())

    def display(self):
        print(self.table)


class Operations:

    def __init__(self, t1 : Table, t2 : Table):
        self.t1 = t1
        self.t2 = t2

    def insert(self, *attributes):
        
        if(len(attributes) == 5):
            if(self.t1.exists(attributes[0])):
                print("Entry already exists!")
                return
            
            self.t1.insert(attributes[0], attributes[1], attributes[2])
            self.t2.insert(attributes[0], attributes[3], attributes[4])
        
        else:
            print("Arguments Mismatch!")
    

    def delete(self, target):
        
        if(not self.t1.exists(target)):
            print("Entry not found!")
            return
        
        else:

            self.t1.delete(target)
            self.t2.delete(target)



    def display(self):

        for _ in range(116):
            print("-", end="")
        print()

        attr1 = self.t1.get_attributes()

        print(f"| {attr1[0]:<20} | ", end= "")

        for attr in attr1[1:]:
            print(f"{attr:<20}", end=" | ")

        for attr in self.t2.get_attributes()[1:]:
            print(f"{attr:<20}", end=" | ")

        print()

        for _ in range(116):
            print("-", end="")
        print()
        
        keys1 = self.t1.get_keys()
        for key in keys1:
            print(f"| {key:<20} | ", end = "")
            for value in self.t1.get_value(key):
                print(f"{value:<20}", end=" | ")
            for value in self.t2.get_value(key):
                print(f"{value:<20}", end=" | ")
            print()

        for _ in range(116):
            print("-", end="")
        print()
        


def main():

    t1 = Table("Enrollment No.", "Name", "Contact")
    t2 = Table("Enrollment No.", "Course Code", "Marks")

    op = Operations(t1, t2)

    while(True):
        print("1. Insert an entry.")
        print("2. Delete an entry.")
        print("3. Display Entries.")
        print("4. exit")
        inp = input("Enter of choice number : ")
        if(inp == "1"):
            enrollment_no = input("Enter enrollment no. : ")
            name = input("Enter name : ")
            contact = input("Enter phone number : ")
            subject_code = input("Enter subject code : ")
            marks = input("Enter marks : ")
            op.insert(enrollment_no, name, contact, subject_code, marks)
        elif(inp == "2"):
            enrollment_no = input("Enter enrollment no. : ")
            op.delete(enrollment_no)
        elif(inp == "3"):
            op.display()
        elif(inp == "4"):
            break
        else:
            print("Invalid choice!")
        print()

if(__name__ == "__main__"):
    main()