import os
import shutil
import hashlib
import time

class FilesSync:
    def __init__(self, source_path: str, replica_path: str, sync_time: int, log_path: str) -> None:
        self.source_path = source_path
        self.replica_path = replica_path
        self.sync_time = sync_time,
        self.log_path = log_path
    
    def start_sync(self) -> None:
        while True:

            self.validate_paths()
            # Get files from directories (Just files)
            source_files = [file for file in os.listdir(self.source_path) if os.path.isfile(os.path.join(self.source_path, file))]
            replica_files = [file for file in os.listdir(self.replica_path) if os.path.isfile(os.path.join(self.replica_path, file))]

            for file in source_files:
                source_file_path = os.path.join(self.source_path, file)
                replica_file_path = os.path.join(self.replica_path, file)
                if file in replica_files:
                    if self.compare_two_files(source_file_path, replica_file_path):
                        print(f'File {file} already in {self.replica_path}')
                    else:
                        shutil.copy2(source_file_path, self.replica_path)
                        print(f'File {file} updated in {self.replica_path}')
                else:
                    shutil.copy2(source_file_path, self.replica_path)
                    print(f'File {file} added to {self.replica_path}')
                

            for file in replica_files:
                if file not in source_files:
                    # remove files from replica
                    replica_file_path = os.path.join(self.replica_path,file)
                    os.remove(replica_file_path)
                    print(f'File {file} removed from {self.replica_path}')

            time.sleep(self.sync_time)
    
    def validate_paths(self) -> None:
        for path in [self.source_path, self.replica_path, self.log_path]:
            if not os.path.isdir(path):
                print(f"Path does not exist or is not a directory: '{path}'")
                exit()

    @staticmethod
    def compare_two_files(source_file: str, replica_file: str) -> bool:
        with open(source_file, 'rb') as source:
            with open(replica_file, 'rb') as replica:
                if hashlib.md5(source.read()).hexdigest() == hashlib.md5(replica.read()).hexdigest():
                    return True
                else: 
                    return False
