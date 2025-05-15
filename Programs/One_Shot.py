import sys
print()
# Printing Hello World
# print("Hello World")

# Using Escape Sequence
# print("Hello\nWorld")

# Single Line Comment
# This is a single line comment

# Multiline Comments
'''
This is a multiline comment
'''

# REPL :- Read Evaluate Print Loop

# Variables and Datatypes

# x = 5           # Integer
# y = "Hello"     # String
# z = 5.2         # Float
# a = True        # Boolean
# b = None        # None
# c = 3 + 4j      # Complex

# name = "Isha"
# roll_number = 17
# percentage = 95.8
# is_student = True

# percentage = 93

# print(name, roll_number, percentage, is_student)
# print(type(name), type(roll_number), type(percentage), type(is_student))
# print("My name is " + name)
# print("My roll number is", roll_number)
# print("My percentage is ", percentage)
# print("Whether I am a student :", is_student)

# print("My percentage is changed to", percentage - 1)

# print(1, 2, 3, sep=" -> ")        # separator


'''
1. Numric datatypes:
    Integer
    Float
    Complex

2. Boolean datatypes

3. Sequence datatypes:
    String
    List
    Tuple

4. Dictionary datatype

5. Set datatype

6. None datatype
'''

# ord() function        char -> ascii
# print(ord('A'))

# chr() function        ascii -> char
# print(chr(65))


# Taking Input

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# print(name, age)

# Program to print sum of two numbers

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# total = num1 + num2
# print(f"The sum of {num1} and {num2} is {total}")



'''
Operators
    Arithmetic 
    Assignment
    Comparison
    Logical
    Identity
    Membership
    Bitwise
'''

'''
Arithmetic Operators:
    Addition (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)
    Modulus (%)
    Exponentiation (**)
    Floor Division (//)
'''

# print("sum :", 4 + 3)
# print("diff :", 4 - 3)
# print("mul :", 4 * 3)
# print("div :", 4 / 3)
# print("modulus :", 4 % 3)
# print("exp :", 4 ** 3)
# print("floor :", 17 // 9)

'''
Assignment Opearators:
    =
    +=
    -=
    *=
    /=
    %=
    //=
    **=
    &=
    |=
    ^=
    >>=
    <<=
'''

'''
Comparison Operators:
    Equal
    Not equal
    Greater than
    Less than
    Greater than or equal to
    Less than or equal to 
'''

# print(4 > 3)

'''
Logical Operators
    and
    or
    not
'''

# print(not(2 > 1))

'''
Identity Operators
    is
    is not
'''

# a = 3
# b = 3
# print(a is b)

'''
Membership Operator
    in
    not in
'''

# print(5 in [1, 2, 4, 5])
# print(3 not in [1, 2, 4, 5])

'''
Bitwise Operators
    and
    or
    xor
    not
    left shift
    right shift
'''

# print(22<<1)
# print(22>>1)

# Program to calculate volume of a sphere

# radius = float(input("Enter the radius of the sphere : "))

# volume = (4/3) * 3.14159 * (radius ** 3)

# print("The volume of the sphere is", volume)

# Operator Precedence

'''
()
**
/
//
*
+
-
Bitwise shift
Bitwise and, or, xor
Comparison
Logical and, or, not
'''

# type() function

# a = 5
# print(type(a))

# Typecasting

# a = 3
# b = float(a)
# print(b)

# Program to convert Celsius to Fahrenheit

# cel = float(input("Enter the temperature in celsius : "))

# fah = (9/5) * cel + 32

# print("The temperature in Fahrenheit is", fah)

# Conditional Statements

# Take an integer and tell if it is positve or negative

# num = int(input("Enter an integer : "))

# if(num > 0):
#     print("The entered number is positive.")
# elif(num == 0):
#     print("The entered number is neither positive nor negative.")
# else:
#     print("The entered number is negative.")

# Take positive integer input and tell if it is even or odd.

# num = int(input("Enter a positive integer : "))

# if(num % 2 == 0):
#     print("The entered number is even.")
# else:
#     print("The entered number is odd.")

# Profit Loss problem

# cp = float(input("Enter the cost price : "))
# sp = float(input("Enter the selling price : "))

# if(sp > cp):
#     profit = sp - cp
#     print(f"The seller made a profit of {profit} rupees.")
# elif(sp == cp):
#     print("The seller made neither profit nor loss.")
# else:
#     print(f"The seller incurrd a loss of {cp - sp} rupees.")

# Printing grade of student

# marks = int(input("Enter the marks of students : "))

# if(marks >= 81):
#     print("Very Good")
# elif(marks >= 61):
#     print("Good")
# elif(marks >= 41):
#     print("Average")
# else:
#     print("Fail")

# Print grade based on a condition

# eng_marks = int(input("Enter English Marks : "))
# maths_marks = int(input("Enter Maths Marks : "))

# if(eng_marks > 80 and maths_marks > 80):
#     print("A Grade.")
# elif(eng_marks > 80 or maths_marks > 80):
#     print("B Grade.")
# else:
#     print("C Grade.")

# Take a positive integer and tell if it is a four digit nubmer or not.

# num = input("Enter a number : ")

# if(len(num) == 4):
#     print("It is a four digit number.")
# else:
#     print("It is NOT a four digit number.")

# Take 3 positive integer inputs and print the greatest of them.

# inter_list = [input(f"Enter number {i} : ") for i in range(1, 4)]
# inter_list.sort()
# print("The largest integer is", inter_list[-1])

# Take a positive integer input and tell if it is divisible by 5 or 3 but not disible by 15

# num = int(input("Enter a positive integer : "))

# if((num % 5 == 0 or num % 3 == 0) and num % 15 != 0):
#     print("Condition met.")
# else:
#     print("Condition NOT met.")

# Match Case


# x = 5
# match x:

#     case 1:
#         print("This is first case.")
#     case 2:
#         print("This is second case.")
#     case _:
#         print("This is default case.")

# Ternary Operator

Boolean = True if (5 > 3) else False

print(Boolean)    
    
print()
# 3:38:33