import hashlib 
import bcrypt


class auth():
     def hash_password(password):
          return hashlib.sha256(password.encode()).hexdigest()

     def verify_password(stored_hash, entered_password):
          return stored_hash == hashlib.sha256(entered_password.encode()).hexdigest()