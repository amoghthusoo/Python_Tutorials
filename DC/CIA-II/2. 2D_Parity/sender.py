import socket

print()
sender_socket = socket.socket()
sender_socket.connect(('localhost', 9999))



dataword_1 = input("Enter the dataword 1 (8 bits): ")
dataword_2 = input("Enter the dataword 2 (8 bits): ")
print()

parity_bit_1 = str(dataword_1.count('1') % 2)
codeword_1 = dataword_1 + parity_bit_1

parity_bit_2 = str(dataword_2.count('1') % 2)
codeword_2 = dataword_2 + parity_bit_2

parity_word = ""
for i in range(len(codeword_1)):
    parity_word += str(int(codeword_1[i]) ^ int(codeword_2[i]))


print("Dataword 1:", dataword_1)
print("Parity bit 1:", parity_bit_1)

print("Dataword 2:", dataword_2)
print("Parity bit 2:", parity_bit_2)

sender_socket.send(codeword_1.encode())
sender_socket.send(codeword_2.encode())
sender_socket.send(parity_word.encode())

print("Codeword 1 sent:", codeword_1)
print("Codeword 2 sent:", codeword_2)
print("Parity word sent:", parity_word)
print("\n")