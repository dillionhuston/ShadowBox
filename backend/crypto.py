from cryptography.fernet import Fernet
class cryptomanager:

    def __init__(self ):
        def generate_key(self):
            key = Fernet.generate_key()
            with open('key.txt', 'wb') as key_file:
                key_file.write(key)

                return key