import socket

print()
sender_socket = socket.socket()
sender_socket.connect(('localhost', 9999))

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

dataword = input("Enter the dataword (8 bits): ")
divisor = "101"
remainder = get_remainder(dataword, divisor)
codeword = dataword + remainder
print("Dataword:", dataword)

sender_socket.send(codeword.encode())

print("Codeword sent:", codeword)
print()

