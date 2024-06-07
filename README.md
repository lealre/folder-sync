# Folder Synchronization for File Backup

This repository hosts an implementation of a program designed to synchronize two folders: a source and a replica.

The program's objective is to ensure that the replica folder maintains a complete, identical copy of the source folder.

- Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;
- Synchronization should be performed periodically;
- File creation/copying/removal operations should be logged to a file and to the console output;
- Folder paths, synchronization interval and log file path should be provided using the command line arguments;

This synchronization is achieved using only built-in Python libraries.

## How to run locally

All the steps here are intended to a `bash` terminal.

1. Clone the repository locally
```bash
git clone https://github.com/lealre/folder-sync.git
```

2. Enter the project folder
```bash
cd folder-sync
```

3. Set the local Python version (Optional - Requires [`pyenv`](https://github.com/pyenv/pyenv))
```bash
pyenv local 3.12.2
```

As it uses just built-in Python packages, steps 4 and 5 are optional.

4. Create a virtual environment (Optional)
```bash
python -m venv .venv
```

5. Activate virtual environment (Optional)
```bash
 source .venv/bin/activate
```

6. Run the program locally by replacing the actual source folder path with <SOURCE_FOLDER_PATH>, the replica folder path with <REPLICA_FOLDER_PATH>, the log file path with <FILE_PATH>, and the synchronization interval with <SYNC_INTERVAL>

```bash
python app --source_path=<SOURCE_FOLDER_PATH> --replica_path=<REPLICA_FOLDER_PATH> --log_path=<FILE_PATH> --sync_time=<SYNC_INTERVAL>
```

To run it as it is in the cloned project, simply execute the following command
```bash
python app  --source_path=data/source --replica_path=data/replica --log_path=logs/log.txt --sync_time=10
```