import time

class Logs:
    def __init__(self, log_path:str) -> None:
        self.log_path = log_path

    def start_log(self, source_path, replica_path) -> None:
        self.log_message("Synchronization started")
        self.log_message(f'Synchronizing from {source_path} to {replica_path}')
    
    def log_count_changes(self, replica_path: str) -> None:
        self.replica_path = replica_path
        self.register = {
            'added': 0,
            'updated': 0,
            'removed': 0
            }
    
    def log_add(self, file) -> None:
        self.log_message(f"File {file} added to {self.replica_path}")
        self.register["added"] += 1
    
    def log_remove(self, file) -> None:
        self.log_message(f"File {file} removed from {self.replica_path}")
        self.register["removed"] += 1
    
    def log_update(self, file) -> None:
        self.log_message(f"File {file} updated in {self.replica_path}")
        self.register["updated"] += 1
    
    def log_register_changes(self) -> None:
        self.log_message(f"{self.register['added']} files added, {self.register['updated']} files updated, {self.register['removed']} files removed")
    
    def stop_log(self) -> None:
        self.log_message("Synchronization stopped")
        with open(self.log_path, 'a') as f:
            f.write("--------------------")

    def log_message(self, message) -> None:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_message = f'[{now}]: {message}'
        print(log_message)
        log_message += '\n'
        with open(self.log_path, 'a') as f:
            f.write(log_message)