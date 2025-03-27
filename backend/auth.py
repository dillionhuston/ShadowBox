import hashlib 
import bcrypt


class auth():
     def hash_password(self, password):
        # It's a good idea to use bcrypt rather than sha256 for hashing passwords
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode('utf-8')

     def verify_password(self, stored_hash, entered_password):
        # Verify password using bcrypt
        return bcrypt.checkpw(entered_password.encode(), stored_hash.encode())