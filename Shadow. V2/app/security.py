from passlib.hash import pbkdf2_sha256
from typing import Optional

class PasswordTools:
    """Contain password related function."""
    
    @staticmethod
    def HashPassword(raw_password: str) -> Optional[str]:
        """Hash the given password, using pbkdf2_sha256.

        Args:
            raw_password (str): The raw (plain) password to hash.

        Returns:
            Optional[str]: The result hashed password, or None if failed.
        """
        #? Can we... use CryptContext + bcrypt? It's more safer (ChatGPT say).
        try:
            return pbkdf2_sha256.hash(raw_password)
        except Exception as e:
            # This part shouldn't be executed for now.
            # Just future preparation.
            print(f"Exception occurred ({type(e).__name__}): {str(e)}")
            return None

    @staticmethod
    def VerifyHash(check_raw_password: str, hashed_password: str) -> bool:
        """Verify the given raw (plain) password matched the hashed password.

        Args:
            check_raw_password (str): The raw (plain) password to check.
            hashed_password (str): The hashed password.

        Returns:
            bool: True if match, False otherwise (or failed).
        """
        try:
            return pbkdf2_sha256.verify(check_raw_password, hashed_password)
        except Exception as e:
            # This part shouldn't be executed for now.
            # Just future preparation.
            print(f"Exception occurred ({type(e).__name__}): {str(e)}")
            return False
