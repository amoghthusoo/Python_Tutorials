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

def get_remainder(dataword, divisor):
    
    dataword = dataword + '0' * (len(divisor) - 1)
    dataword = list(dataword)
    divisor = list(divisor)

    for i in range(len(dataword) - len(divisor) + 1):
        if dataword[i] == '1':
            for j in range(len(divisor)):
                dataword[i + j] = str(int(dataword[i + j]) ^ int(divisor[j]))

    remainder = ''.join(dataword[-(len(divisor) - 1):])
    return remainder


divisor = "101"
codeword = connection.recv(8 + len(divisor)).decode()

codeword = "0" + codeword[1:]

remainder = get_remainder(codeword, divisor)

if(remainder == "0" * (len(divisor) - 1)):
    print("Codeword received:", codeword)
    print("Dataword:", codeword[:-len(divisor) + 1])
    print("Remainder:", remainder)
    print("No error in codeword.")
else:
    print("Codeword received:", codeword)
    print("Dataword:", codeword[:-len(divisor) + 1])
    print("Remainder:", remainder)
    print("Error in codeword.")
    
print()