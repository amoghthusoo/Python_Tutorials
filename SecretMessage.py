class SecretMessage:
    def __init__(self, message, algorithm):
        self.message = message
        self.algorithm = algorithm
    def initialize(self):
        if self.algorithm in ['e', 'E']:
            return self.encrypt()
        elif self.algorithm in ['d', 'D']:
            return self.decrypt()
        else:
            return "INVALID INPUT!"
    def encrypt(self):
        encrypted_message = ''
        for letter in self.message:
            encrypted_message += chr(ord(letter) + 1)
        return encrypted_message
    def decrypt(self):
        decrypted_message = ''
        for letter in self.message:
            decrypted_message += chr(ord(letter) - 1)
        return decrypted_message
def main():
    input_string = input("\nEnter the message : ")
    algorithm = input("Enter the Algorithm for Encryption or Decryption (e/d) : ")
    obj = SecretMessage(input_string, algorithm)
    out = obj.initialize()
    print("\n" + out + "\n")
if __name__ == "__main__":
    main()   