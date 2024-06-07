# folder-sync

### Task

Implement a program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of source folder at replica folder.

- Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;
- Synchronization should be performed periodically;
- File creation/copying/removal operations should be logged to a file and to the console output;
- Folder paths, synchronization interval and log file path should be provided using the command line arguments;

### Steps
```bash
pyenv local 3.12.2
```
```bash
python -m venv .venv
```
```bash
 source .venv/bin/activate
```
```bash
python src/main.py --source_path=data/source --replica_path=data/replica --log_path=logs/log.txt --sync_time=10
```