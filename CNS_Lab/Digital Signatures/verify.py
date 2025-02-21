from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def load_public_key(file_path):
    with open(file_path, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read()
        )
    return public_key

def verify_file(file_path, signature_path, public_key):

    with open(file_path, "rb") as f:
        file_data = f.read()

    with open(signature_path, "rb") as f:
        signature = f.read()

    digest = hashes.Hash(hashes.SHA256())
    digest.update(file_data)
    hash_msg = digest.finalize()   

    try:
        public_key.verify(
            signature,
            hash_msg, 
            padding.PSS(
                mgf = padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Signature is valid! File is authentic.")
    except:
         print("Signature is INVALID! File may be tampered with.")

def main():

    file_path = input("Enter the file's path, to be verified : ")
    print()
    
    public_key = load_public_key(r"CNS_Lab\Digital Signatures\public_key.pem")
    verify_file(file_path, r"CNS_Lab\Digital Signatures\signature.sig", public_key)

if(__name__ == "__main__"):
    print()
    main()
    print()
