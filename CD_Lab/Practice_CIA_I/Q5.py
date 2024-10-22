t1 = dict()
t2 = dict()
while(True):
    print("1. Enter a new entry.")
    print("2. Delete an existing entry.")
    print("3. Display all entries.")
    print("4. Exit")
    choice = input("Enter your choice : ")

    if(choice == "1"):
        
        enrollment_no = input("Enter enrollment no. : ")
        name = input("Enter name : ")
        contact = input("Enter contact : ")
        course_code = input("Enter course code : ")
        marks = input("Enter marks : ")

        if(enrollment_no not in t1):
            t1[enrollment_no] = [name, contact]
            t2[enrollment_no] = [course_code, marks]

        else:
            print("Entry already exists!")

    elif(choice == "2"):
        
        enrollment_no = input("Enter the enrollment no. : ")

        if(enrollment_no in t1):
            t1.pop(enrollment_no)
            t2.pop(enrollment_no)
        else:
            print("Entry not found!")

    elif(choice == "3"):
        
        for enrollment, record in t1.items():
            print(f"{enrollment} : {record[0]} | {record[1]} | {t2[enrollment][0]} | {t2[enrollment][1]}")

    elif(choice == "4"):
        break

    else:
        print("Invalid Input!")
    
    print()