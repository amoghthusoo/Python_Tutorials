import socket

sender_socket = socket.socket()
sender_socket.connect(('localhost', 9999))

file_path = r"C:\Users\Dell\Desktop\Python_Tutorials\DC\Assignment_1\data.txt"

with open (file_path, 'r') as file:
    data = file.read()

total_len = len(data)

x = total_len // 3
first_part = data[0 : x]
second_part = data[x : 2 * x]
third_part = data[2 * x :]

first_part_len = len(first_part)
second_part_len = len(second_part)
third_part_len = len(third_part)

print()
print(f"Length of data : {total_len}")
print(f"Length of first part : {first_part_len}")
print(f"Length of second part : {second_part_len}")
print(f"Length of third part : {third_part_len}")
print()

sender_socket.send(f"{str(first_part_len)} {str(second_part_len)} {str(third_part_len)}".encode())

sender_socket.send(first_part.encode())
print("First part sent successfully.")

sender_socket.send(second_part.encode())
print("Second part sent successfully.")

sender_socket.send(third_part.encode())
print("Third part sent successfully.")
print()
