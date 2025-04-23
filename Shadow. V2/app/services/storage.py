#file sotrage and retrival logic
import logging
import os 
from config import Config

encrypted_file_path = Config.ENCRYPTED_FILE_PATH  


class FileStorageService:

    @staticmethod
    def save_file(self, file_data):
        if file is None:
            logging.error("no file")
            return
        else:
            path = os.path.join(filename)
            with open(encrypted_file_path, 'wb') as file:
                file.write(file_data)
        return
      
    def retrieve_file(self, file_id):
        # Logic to retrieve files
        pass