from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

with open(r"CNS_Lab\CIA1_Practice\data.txt", "rb") as f:
    data = f.read()

digest = hashes.Hash(hashes.SHA256())
digest.update(data)
hashed_msg = digest.finalize()

signature = private_key.sign(
    hashed_msg, 
    padding.PSS(
        mgf = padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )

# with open(r"CNS_Lab\CIA1_Practice\data.txt", "a") as f:
#     data = f.write("temp")

with open(r"CNS_Lab\CIA1_Practice\data.txt", "rb") as f:
    data = f.read()

digest = hashes.Hash(hashes.SHA256())
digest.update(data)
hashed_msg = digest.finalize()

try:
    public_key.verify(
        signature,
        hashed_msg,
        padding.PSS(
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length = padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
except:
    print("Given file has been tampared.")
    quit()

print("Given file is authentic.")