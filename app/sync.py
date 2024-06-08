import os
import shutil
import hashlib
import time

from log import Logs

class FolderSync(Logs):
    """
    Synchronizes files between a source folder and a replica folder.

    Inherits from Logs class for logging functionality.
    
    Attributes:
        source_path (str): The path to the source folder.
        replica_path (str): The path to the replica folder.
        sync_time (int): The time interval between synchronization attempts (in seconds).
        log_path (str): The path to the log file for logging synchronization events.
    """
    
    def __init__(self, source_path: str, replica_path: str, sync_time: int, log_path: str) -> None:
        super().__init__(log_path = log_path, 
                         replica_path= replica_path)
        self.source_path = source_path
        self.replica_path = replica_path
        self.sync_time = sync_time 
    
    def start_sync(self) -> None:
        """
        Starts the synchronization process.

        Validates paths, starts logging, and continuously compares folders.
        Stops logging when a KeyboardInterrupt is raised.
        """
        self.validate_paths()
        try:
            self.start_log(self.source_path, self.replica_path)
            while True:
                self.compare_folders()   
                time.sleep(self.sync_time)
        except KeyboardInterrupt:
            self.stop_log()
    
    def compare_folders(self):
        """
        Compares files between source and replica folders, updating replica files as needed.
        
        Logs additions, updates, and removals of files, and updates counters accordingly.
        """
        source_files, replica_files = self.get_files()

        for file in source_files:
            source_file_path = os.path.join(self.source_path, file)
            replica_file_path = os.path.join(self.replica_path, file)
            if file in replica_files:
                if not self.compare_two_files(source_file_path, replica_file_path):
                    try:
                        shutil.copy2(source_file_path, self.replica_path)
                        self.log_update(file)
                    except Exception as e:
                        self.log_error(e, file)
            else:
                try:
                    shutil.copy2(source_file_path, self.replica_path)
                    self.log_add(file)
                except Exception as e:
                    self.log_error(e, file)

        for file in replica_files:
            if file not in source_files:
                replica_file_path = os.path.join(self.replica_path,file)
                try:
                    os.remove(replica_file_path)
                    self.log_remove(file)
                except Exception as e:
                    self.log_error(e, file)

        self.log_register_counter()

    def validate_paths(self) -> None:
        """
        Validates the existence and type of paths.

        Exits the program if any path does not exist or is not of the expected type.
        """
        for path in [self.source_path, self.replica_path]:
            if not os.path.isdir(path):
                print(f"Path does not exist or is not a directory: '{path}'")
                exit()
        if not os.path.isfile(self.log_path):
                print(f"Path does not exist or is not a file: '{self.log_path}'")
                exit()
    
    def get_files(self) -> tuple:
        """
        Retrieves the list of files from the source and replica paths.

        Returns:
            tuple: A tuple containing two lists of files.
                The first list contains files from the source path,
                and the second list contains files from the replica path.
        """
        try:
            source_files = [file for file in os.listdir(self.source_path) if os.path.isfile(os.path.join(self.source_path, file))]
        except Exception as e:
            self.log_error(e, self.source_path)
        
        try:
            replica_files = [file for file in os.listdir(self.replica_path) if os.path.isfile(os.path.join(self.replica_path, file))]
        except Exception as e:
            self.log_error(e, self.replica_path)
        
        return source_files, replica_files

    def compare_two_files(self, source_file: str, replica_file: str) -> bool:
        """
        Compares the contents of two files using MD5 hashes.

        Args:
            source_file (str): The path to the source file.
            replica_file (str): The path to the replica file.

        Returns:
            bool: True if the files have the same content, False otherwise.
        """
        try:
            with open(source_file, 'rb') as source:
                with open(replica_file, 'rb') as replica:
                    if hashlib.md5(source.read()).hexdigest() == hashlib.md5(replica.read()).hexdigest():
                        return True
                    else: 
                        return False
        except Exception as e:
            self.log_error(e, [source_file, replica_file])