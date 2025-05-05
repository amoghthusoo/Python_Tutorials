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

# codeword = "0" + codeword[1:]

dataword = codeword[:-1]
parity_bit = codeword[-1]

calculated_parity_bit = str(dataword.count('1') % 2)

if(parity_bit == calculated_parity_bit):
    print("Codeword received:", codeword)
    print("Dataword:", dataword)
    print("Received parity bit:", parity_bit)
    print("Calculated parity bit:", calculated_parity_bit)
    print("No error detected.")
else:
    print("Codeword received:", codeword)
    print("Dataword:", dataword)
    print("Received parity bit:", parity_bit)
    print("Calculated parity bit:", calculated_parity_bit)
    print("Error detected in the codeword.")
print()