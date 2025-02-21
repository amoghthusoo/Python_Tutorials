from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def load_private_key(file_path):
    with open(file_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None
        )
    return private_key

def sign_file(file_path, private_key, signature_path):

    with open(file_path, "rb") as f:
        file_data = f.read()

    digest = hashes.Hash(hashes.SHA256())
    digest.update(file_data)
    hashed_msg = digest.finalize()

    signature = private_key.sign(
        hashed_msg,
        padding.PSS(
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open(signature_path, "wb") as f:    
        f.write(signature)

    print(f"File '{file_path}' signed successfully! Signature saved in '{signature_path}'.")

def main():
    
    file_path = input("Enter the file's path, to be signed : ")
    print()

    private_key = load_private_key(r"CNS_Lab\Digital Signatures\private_key.pem")
    sign_file(file_path, private_key, r"CNS_Lab\Digital Signatures\signature.sig")

if(__name__ == "__main__"):
    print()
    main()
    print()
