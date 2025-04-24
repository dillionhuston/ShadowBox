#file sotrage and retrival logic
import logging
import os 
from config import Config

encrypted_file_path = Config.ENCRYPTED_FILE_PATH  


class FileStorageService:
    #currently not used but possibly in future?

    def create_hash_file(self, file):
        return file


    @staticmethod
    def read_file(filedata):
        if filedata is None:
            logging.error("no data")
        else:
            with open(filedata, 'rb')as f:
                data = f.read()
                f.close()
                logging.warn("loaded data")
                return data


    @staticmethod
    def save_file(file_data:bytes, filename):
        if file_data is None:
            logging.error("no file")
            
        else:
            path = os.path.join(encrypted_file_path, filename + '.enc')
            with open(path, 'wb') as file:
                file.write(file_data)
                file.close()
        return
      
    def retrieve_file(self, file_id):
        pass
      
   