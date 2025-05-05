import socket

print()
sender_socket = socket.socket()
sender_socket.connect(('localhost', 9999))


dataword = input("Enter the dataword (8 bits): ")
parity_bit = str(dataword.count('1') % 2)
codeword = dataword + parity_bit

print("Dataword:", dataword)
print("Parity bit:", parity_bit)

sender_socket.send(codeword.encode())

print("Codeword sent:", codeword)
print()