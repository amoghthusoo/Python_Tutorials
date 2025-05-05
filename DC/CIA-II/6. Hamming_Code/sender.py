import socket

print()
sender_socket = socket.socket()
sender_socket.connect(('localhost', 9999))


dataword = input("Enter the dataword (8 bits): ")


print()