import socket

receiver_socket = socket.socket()
receiver_socket.bind(('localhost', 9999))
receiver_socket.listen(1)

print()
print('Waiting for connection...')
connection, address = receiver_socket.accept()
print('Connected to', address)

lengths = connection.recv(1024).decode().split()

first_part_len = int(lengths[0])
second_part_len = int(lengths[1])
third_part_len = int(lengths[2])

print()
print(f"Length of first part : {first_part_len}")
print(f"Length of second part : {second_part_len}")
print(f"Length of third part : {third_part_len}")
print(f"Total length :  {first_part_len + second_part_len + third_part_len}")
print()

first_part = connection.recv(first_part_len).decode()
print("First part received successfully.")

second_part = connection.recv(second_part_len).decode()
print("Second part received successfully.")

third_part = connection.recv(third_part_len).decode()
print("Third part received successfully.")
print()

data = first_part + second_part + third_part

with open ('received_data.txt', 'w') as file:
    file.write(data)

print("Received data written to 'received_data.txt'.")
print()

print("")