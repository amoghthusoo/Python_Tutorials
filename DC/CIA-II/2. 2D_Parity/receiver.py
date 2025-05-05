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


codeword_1 = connection.recv(9).decode()
codeword_2 = connection.recv(9).decode()
parity_word = connection.recv(9).decode()

# codeword_1 = "0" + codeword_1[1:]

calcated_parity_word = ""
for i in range(len(codeword_1)):
    calcated_parity_word += str(int(codeword_1[i]) ^ int(codeword_2[i]))

if(parity_word != calcated_parity_word):
    print("Codeword 1:", codeword_1)
    print("Codeword 2:", codeword_2)
    print("Received parity word:", parity_word)
    print("Calculated parity word:", calcated_parity_word)
    print("Error detected in the parity word.")
    print()
    exit()

dataword_1 = codeword_1[:-1]
parity_bit_1 = codeword_1[-1]

dataword_2 = codeword_2[:-1]
parity_bit_2 = codeword_2[-1]

calculated_parity_bit_1 = str(dataword_1.count('1') % 2)
calculated_parity_bit_2 = str(dataword_2.count('1') % 2)

if(parity_bit_1 == calculated_parity_bit_1 and parity_bit_2 == calculated_parity_bit_2):
    print("Codeword 1 received:", codeword_1)
    print("Dataword 1:", dataword_1)
    print("Parity bit 1:", parity_bit_1)

    print("Codeword 2 received:", codeword_2)
    print("Dataword 2:", dataword_2)
    print("Parity bit 2:", parity_bit_2)

    print("No error detected in the codewords.")

else:
    print("Codeword 1 received:", codeword_1)
    print("Dataword 1:", dataword_1)
    print("Parity bit 1:", parity_bit_1)

    print("Codeword 2 received:", codeword_2)
    print("Dataword 2:", dataword_2)
    print("Parity bit 2:", parity_bit_2)

    print("Error detected in the codewords.")

print("\n")