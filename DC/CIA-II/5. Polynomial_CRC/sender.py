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

dataword_polynomial = input("Enter the dataword polynomial d(x) (8 bits): ")
dataword_arr = ["0" for _ in range(8)] 

try:
    i = 0
    while(i < len(dataword_polynomial)):

        if(dataword_polynomial[i] == "^"):
            dataword_arr[int(dataword_polynomial[i + 1])] = "1"

        i += 1
except:
    print("Invalid input. Please enter a valid polynomial in the form of d(x) = x^n + x^m + ... + x^0")
    print()
    exit()

dataword = ''.join(dataword_arr)[-1::-1]

divisor = "101"
remainder = get_remainder(dataword, divisor)
codeword = dataword + remainder
print("Dataword:", dataword)

sender_socket.send(codeword.encode())

print("Codeword sent:", codeword)
print()

