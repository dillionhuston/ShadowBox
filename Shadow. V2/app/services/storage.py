#file sotrage and retrival logic
import logging
import os 
from config import Config

encrypted_file_path = Config.ENCRYPTED_FILE_PATH
path = "/"


class FileStorageService:
    @staticmethod
    def get_dir_file(self):
        DIR_DATA = os.listdir(path)
        print(DIR_DATA)


    @staticmethod
    def save_file(file_data:bytes, filename):
        if file_data: None, logging.error("no file")
        path = os.path.join(encrypted_file_path, filename + '.enc')
        with open(path, 'wb') as file:
            file.write(file_data)
            file.close()
            return
        
    def retrieve_file(self, file_id):
        pass
      
   