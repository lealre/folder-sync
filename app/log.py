import time
from typing import List, Union

class Logs:
    def __init__(self, log_path:str, replica_path: str) -> None:
        self.log_path = log_path
        self.log_replica_path: str = replica_path
        self.counter: dict = {
            'added': 0,
            'updated': 0,
            'removed': 0
        }

    def start_log(self, source_path, replica_path) -> None:
        """
        Starts logging the synchronization process.

        Args:
            source_path (str): The path from which files are synchronized.
            replica_path (str): The path to which files are synchronized.
        """
        self.log_message("Synchronization started")
        self.log_message(f"Synchronizing from '{source_path}' to '{replica_path}'")
    
    def log_add(self, file) -> None:
        """
        Logs the addition of a file to the replica path.

        Args:
            file (str): The name of the file that was added.
        """
        self.log_message(f"File '{file}' added to '{self.log_replica_path}'")
        self.counter["added"] += 1
    
    def log_remove(self, file) -> None:
        """
        Logs the removal of a file from the replica path.

        Args:
            file (str): The name of the file that was removed.
        """
        self.log_message(f"File '{file}' removed from '{self.log_replica_path}'")
        self.counter["removed"] += 1
    
    def log_update(self, file) -> None:
        """
        Logs the update of a file in the replica path.

        Args:
            file (str): The name of the file that was updated.
        """
        self.log_message(f"File '{file}' updated in '{self.log_replica_path}'")
        self.counter["updated"] += 1
    
    def log_register_counter(self) -> None:
        """
        Logs the counts of added, updated, and removed files, and resets the counter.
        """
        self.log_message(f"{self.counter['added']} file(s) added, "
                         f"{self.counter['updated']} file(s) updated, " 
                         f"{self.counter['removed']} file(s) removed")
        self.counter: dict = {
            'added': 0,
            'updated': 0,
            'removed': 0
        }
    
    def log_error(self, e: Exception, file: Union[str, List[str]]) -> None:
        """
        Logs an error message along with the file(s) involved in the operation that caused the error.
        
        Args:
            e (Exception): The exception that occurred.
            file (Union[str, List[str]]): The file or list of files involved in the operation.
                If multiple files are involved, they are joined with commas.
        """
        if isinstance(file, list):
            file = ', '.join(file)
        
        self.log_message(f"!ERROR occurred during operation with file(s) '{file}'")
        self.log_message(f"Error: {str(e)}")
        self.stop_log()
    
    def stop_log(self) -> None:
        """
        Logs a message indicating that synchronization has stopped and appends a separator line to the log file.
        Then, exits the program.
        """
        self.log_message("Synchronization stopped")
        with open(self.log_path, 'a') as f:
            f.write(20 * "-" + "\n")
        exit()
    
    def log_message(self, message) -> None:
        """
        Logs a message with a timestamp to the console and a log file.

        Args:
            message (str): The message to be logged.
        """
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_message = f'[{now}]: {message}'
        print(log_message)
        log_message += '\n'
        with open(self.log_path, 'a') as f:
            f.write(log_message)