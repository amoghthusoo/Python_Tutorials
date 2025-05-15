from random import shuffle

alphabets = [chr(e) for e in range(97, 123)]
shuffle(alphabets)
encrypt_dict = dict(zip(alphabets, [chr(e) for e in range(97, 123)]))
decrypt_dict = dict(zip([chr(e) for e in range(97, 123)], alphabets))

encrypt = lambda s : "".join([encrypt_dict[e] for e in s])
decrypt = lambda s : "".join([decrypt_dict[e] for e in s])

cipher_text = encrypt(input("Enter the plain text : "))
plain_text = decrypt(cipher_text)
print(f"Cipher Text : {cipher_text}", f"Plain Text : {plain_text}", sep="\n")