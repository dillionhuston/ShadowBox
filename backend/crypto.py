from cryptography.fernet import Fernet

class cryptomanager:
    def __init__(self):
        self.data_path = 'backend/data.db'
        self.key_path = 'key.txt'
        self.key = self.load_or_generate_key()
        self.fernet = Fernet(self.key)


    def load_or_generate_key(self):
        try:
            with open(self.key_path, 'rb') as key_file:
                key = key_file.read().strip()  
                if len(key) != 44: 
                    raise ValueError("Invalid key length. Generating a new key.")
                print(f'Loaded key: {key}')
        except (FileNotFoundError, ValueError):
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as key_file:
                key_file.write(key)
            print(f'Generated and saved new key: {key}')
        return key

    def get_unencrypted_data(self, data: bytes):
        return data
        
        
    def encrypt(self, data):  
        print("calling encrpy")
        from backend.storage import storage
        storage = storage()
        if data is None:
            print("No data to encrypt.")
            return None
        self.encrypted_data = self.fernet.encrypt(data)
        print(self.encrypted_data)
        storage.save_file_to_db(self.encrypted_data)
        return self.encrypted_data
    
       
        
       
         
       

    def decrypt(self):
        """Decrypt the stored encrypted data."""
        # need to implement function for extacting from databse
        #this function just a placeholder for now
        if self.encrypted_data is None:
            print("No data to decrypt.")
            return None
        
        decrypted_data = self.fernet.decrypt(self.encrypted_data)
        print(f'Decrypted data: {decrypted_data}')
        return decrypted_data

