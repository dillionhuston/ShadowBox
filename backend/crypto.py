from cryptography.fernet import Fernet
class cryptomanager:
    def __init__(self ):

     e_path = self.encryted_data_path = "data.bin"
     key = self.key = Fernet.generate_key()


    #pass data to be encrypted, encrypted data path
    def encrypt(self, data, e_path):
        encryped_data = Fernet.encrypt(data)
        with open(e_path, 'wb') as file:
            file.write(encryped_data)
            print(f'Encrypted data: {encryped_data}')
            
        
        def generate_key(self, key):
            with open('key.txt', 'wb') as key_file:
                key_file.write(key)
                return key
            
        def load_key(self):
            with open('key.txt', 'rb') as key_file:
                key = key_file.read()
                print(f'Loaded key: {key}')
                Fernet = Fernet(key)
            

              