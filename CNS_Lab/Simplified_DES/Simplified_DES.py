def P10(K : str) -> str:
    return K[2] + K[4] + K[1] + K[6] + K[3] + K[9] + K[0] + K[8] + K[7] + K[5]

def split(s : str) -> tuple[str, str]:
    
    n = len(s) // 2
    return s[ : n], s[n : ]

def shift(s : str, n : int) -> str:
    return s[n : ] + s[ : n]

def P8(K : str) -> str:
    return K[5] + K[2] + K[6] + K[3] + K[7] + K[4] + K[9] + K[8]

def generate_keys(K : str) -> tuple[str, str]:

    P10_K = P10(K)
    P10_K_left, P10_K_right = split(P10_K)

    P10_K_left_shifted_1 = shift(P10_K_left, 1)
    P10_K_right_shifted_1 = shift(P10_K_right, 1)
    K1 = P8(P10_K_left_shifted_1 + P10_K_right_shifted_1)

    P10_K_left_shifted_2 = shift(P10_K_left_shifted_1, 2)
    P10_K_right_shifted_2 = shift(P10_K_right_shifted_1, 2)
    K2 = P8(P10_K_left_shifted_2 + P10_K_right_shifted_2)

    return K1, K2

########################################################################################################################
def IP(s : str) -> str:
    return s[1] + s[5] + s[2] + s[0] + s[3] + s[7] + s[4] + s[6]

def EP(s : str) -> str:
    return s[3] + s[0] + s[1] + s[2] + s[1] + s[2] + s[3] + s[0]

def XOR(s1 : str, s2 : str) -> str:
    
    xor_result = ""

    for i in range(len(s1)):
        xor_result += str(int(s1[i]) ^ int(s2[i]))
    
    return xor_result

def S0(s : str) -> str:
    
    r = int(s[0] + s[3], 2)
    c = int(s[1] + s[2], 2)

    matrix = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]

    return bin(matrix[r][c])[2:].zfill(2)

def S1(s : str) -> str:
    
    r = int(s[0] + s[3], 2)
    c = int(s[1] + s[2], 2)

    matrix = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]

    return bin(matrix[r][c])[2:].zfill(2)

def P4(s : str) -> str:
    return s[1] + s[3] + s[2] + s[0]    

def IP_inverse(s : str) -> str:
    return s[3] + s[0] + s[2] + s[4] + s[6] + s[1] + s[7] + s[5]

########################################################################################################################

def encrypt(P : str, K1 : str, K2 : str) -> str:

    IP_P = IP(P)

    keys = [K1, K2]

    for i in range(2):
        L, R = split(IP_P)
        EP_R = EP(R)

        XOR_EP_R_K = XOR(EP_R, keys[i])

        XOR_EP_R_K_left, XOR_EP_R_K_right = split(XOR_EP_R_K)

        s0 = S0(XOR_EP_R_K_left)
        s1 = S1(XOR_EP_R_K_right)

        s0_s1 = s0 + s1
        P4_s0_s1 = P4(s0_s1)

        XOR_P4_s0_s1_L =  XOR(P4_s0_s1, L)
        
        if(i != 1):
            end_result = R + XOR_P4_s0_s1_L
            IP_P = end_result
        else:
            end_result = XOR_P4_s0_s1_L + R

    IP_inverse_end_result = IP_inverse(end_result)
    return IP_inverse_end_result


def decrypt(C : str, K1 : str, K2 : str) -> str:

    IP_C = IP(C)

    keys = [K2, K1]

    for i in range(2):
        L, R = split(IP_C)
        EP_R = EP(R)

        XOR_EP_R_K = XOR(EP_R, keys[i])

        XOR_EP_R_K_left, XOR_EP_R_K_right = split(XOR_EP_R_K)

        s0 = S0(XOR_EP_R_K_left)
        s1 = S1(XOR_EP_R_K_right)

        s0_s1 = s0 + s1
        P4_s0_s1 = P4(s0_s1)

        XOR_P4_s0_s1_L =  XOR(P4_s0_s1, L)
        
        if(i != 1):
            end_result = R + XOR_P4_s0_s1_L
            IP_C = end_result
        else:
            end_result = XOR_P4_s0_s1_L + R

    IP_inverse_end_result = IP_inverse(end_result)
    return IP_inverse_end_result

########################################################################################################################

def main():
    # P = "10100110"
    # K = "1100101001"

    P = input("Enter the 8-bit plain text (binary) : ")
    K = input("Enter the 10-bit key (binary) : ")
    print()

    K1, K2 = generate_keys(K)

    cipher_text = encrypt(P, K1, K2)

    decrypted_text = decrypt(cipher_text, K1, K2)

    print("Plain Text :", P)
    print("Cipher Text :", cipher_text)
    print("Decrypted Text :", decrypted_text)
    print()

    if(P == decrypted_text):
        print("Decryption is successful.")
    else:
        print("Decryption is unsuccessful.")

if(__name__ == "__main__"):
    print()
    main()
    print()
