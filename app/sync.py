import os
import shutil
import hashlib
import time

from log import Logs

class FolderSync(Logs):
    def __init__(self, source_path: str, replica_path: str, sync_time: int, log_path: str) -> None:
        super().__init__(log_path = log_path, 
                         replica_path= replica_path)
        self.source_path = source_path
        self.replica_path = replica_path
        self.sync_time = sync_time 
    
    def start_sync(self) -> None:
        self.validate_paths()
        try:
            self.start_log(self.source_path, self.replica_path)
            while True:
                self.compare_folders()   
                time.sleep(self.sync_time)
        except KeyboardInterrupt:
            self.stop_log()
    
    def compare_folders(self):
        source_files = [file for file in os.listdir(self.source_path) if os.path.isfile(os.path.join(self.source_path, file))]
        replica_files = [file for file in os.listdir(self.replica_path) if os.path.isfile(os.path.join(self.replica_path, file))]
        for file in source_files:
            source_file_path = os.path.join(self.source_path, file)
            replica_file_path = os.path.join(self.replica_path, file)
            if file in replica_files:
                if not self.compare_two_files(source_file_path, replica_file_path):
                    shutil.copy2(source_file_path, self.replica_path)
                    self.log_update(file)
            else:
                shutil.copy2(source_file_path, self.replica_path)
                self.log_add(file)

        for file in replica_files:
            if file not in source_files:
                replica_file_path = os.path.join(self.replica_path,file)
                os.remove(replica_file_path)
                self.log_remove(file)
        
        self.log_register_counter()

    def validate_paths(self) -> None:
        for path in [self.source_path, self.replica_path]:
            if not os.path.isdir(path):
                print(f"Path does not exist or is not a directory: '{path}'")
                exit()
        if not os.path.isfile(self.log_path):
                print(f"Path does not exist or is not a file: '{self.log_path}'")
                exit()

    @staticmethod
    def compare_two_files(source_file: str, replica_file: str) -> bool:
        with open(source_file, 'rb') as source:
            with open(replica_file, 'rb') as replica:
                if hashlib.md5(source.read()).hexdigest() == hashlib.md5(replica.read()).hexdigest():
                    return True
                else: 
                    return False
