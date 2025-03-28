from cryptography.fernet import Fernet

class cryptomanager:
    def __init__(self):
        self.data_path = '/data/files.db'
        self.key_path = '/data/key.txt'
        self.key = self.load_or_generate_key()
        self.fernet = Fernet(self.key)

    def load_or_generate_key(self):
        """Load an existing key or generate a new one."""
        try:
            with open(self.key_path, 'rb') as key_file:
                key = key_file.read().strip()  # Ensure no extra spaces or newlines
                if len(key) != 44:  # Fernet keys are always 44 characters long
                    raise ValueError("Invalid key length. Generating a new key.")
                print(f'Loaded key: {key}')
        except (FileNotFoundError, ValueError):
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as key_file:
                key_file.write(key)
            print(f'Generated and saved new key: {key}')
        return key

    def get_unencrypted_data(self, data: bytes) -> bytes:
        self.unencrypted = data
        print(f'Unencrypted data: {self.unencrypted}')
        return self.unencrypted

        
        
    def encrypt(self, data):   
        if data is None:
            print("No data to encrypt.")
            return None
       
        encrpted_data = self.fernet.encrypt(self.unencrypted)
        print(encrpted_data)
        return encrpted_data
         
       

    def decrypt(self):
        """Decrypt the stored encrypted data."""
        # need to implement function for extacting from databse


# Example usage
if __name__ == "__main__":
    crypto = cryptomanager()
    crypto.encrypt('plaintext.txt')  # Encrypt a sample text file
    decrypted_data = crypto.decrypt()
    if decrypted_data:
        print("Decrypted content:", decrypted_data.decode())
