import hashlib 
import bcrypt


class auth():
     def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode('utf-8')

     def verify_password(self, stored_hash, entered_password):
        return bcrypt.checkpw(entered_password.encode(), stored_hash.encode())