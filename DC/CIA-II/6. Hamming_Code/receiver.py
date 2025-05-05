import socket

print()
receiver_socket = socket.socket()
receiver_socket.bind(('localhost', 9999))
receiver_socket.listen(1)

print()
print('Waiting for connection...')
connection, address = receiver_socket.accept()
print('Connected to', address)
print()

codeword = connection.recv(1024).decode()

print()