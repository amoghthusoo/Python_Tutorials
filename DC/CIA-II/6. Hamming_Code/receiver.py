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
codeword_arr = list(codeword)

# codeword_arr[2] = '0'
# codeword_arr[4] = '0'

p1 = int(codeword_arr[0]) ^ int(codeword_arr[2]) ^ int(codeword_arr[4]) ^ int(codeword_arr[6]) ^ int(codeword_arr[8]) ^ int(codeword_arr[10])
p2 = int(codeword_arr[1]) ^ int(codeword_arr[2]) ^ int(codeword_arr[5]) ^ int(codeword_arr[6]) ^ int(codeword_arr[9]) ^ int(codeword_arr[10])
p4 = int(codeword_arr[3]) ^ int(codeword_arr[4]) ^ int(codeword_arr[5]) ^ int(codeword_arr[6]) ^ int(codeword_arr[11])
p8 = int(codeword_arr[7]) ^ int(codeword_arr[8]) ^ int(codeword_arr[9]) ^ int(codeword_arr[10]) ^ int(codeword_arr[11])

parity_num = int((str(p8) + str(p4) + str(p2) + str(p1)), 2)

codeword_arr.pop(0)
codeword_arr.pop(0)
codeword_arr.pop(1)
codeword_arr.pop(4)

dataword = ''.join(codeword_arr)


if(parity_num == 0):
    print("Codeword received:", codeword)
    print("Dataword:", dataword)
    print("Received parity bits: ", p8, p4, p2, p1)
    print("No error in the codeword.")
elif(parity_num <= 12):
    print("Codeword received:", codeword)
    print("Dataword:", dataword)
    print("Received parity bits: ", p8, p4, p2, p1)
    print("Error detected in the codeword at position", parity_num)
else:
    print("Codeword received:", codeword)
    print("Dataword:", dataword)
    print("Received parity bits: ", p8, p4, p2, p1)
    print("Error detected in more than one bit in the codeword.")

print()