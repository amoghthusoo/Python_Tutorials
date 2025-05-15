import socket

print()
sender_socket = socket.socket()
sender_socket.connect(('localhost', 9999))

dataword = input("Enter the dataword (8 bits): ")

codeword_arr = list(dataword)

codeword_arr.insert(0, '0')  
codeword_arr.insert(1, '0')  
codeword_arr.insert(3, '0')  
codeword_arr.insert(7, '0')  

# print(codeword_arr)

p1 = int(codeword_arr[2]) ^ int(codeword_arr[4]) ^ int(codeword_arr[6]) ^ int(codeword_arr[8]) ^ int(codeword_arr[10])
p2 = int(codeword_arr[2]) ^ int(codeword_arr[5]) ^ int(codeword_arr[6]) ^ int(codeword_arr[9]) ^ int(codeword_arr[10])
p4 = int(codeword_arr[4]) ^ int(codeword_arr[5]) ^ int(codeword_arr[6]) ^ int(codeword_arr[11])
p8 = int(codeword_arr[8]) ^ int(codeword_arr[9]) ^ int(codeword_arr[10]) ^ int(codeword_arr[11])

codeword_arr[0] = str(p1)
codeword_arr[1] = str(p2)
codeword_arr[3] = str(p4)
codeword_arr[7] = str(p8)

print("Codeword: ", end='')

dataword = ''.join(codeword_arr)
print(dataword)

sender_socket.send(dataword.encode())

print()