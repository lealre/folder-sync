# Folder Synchronization for File Backup

This repository hosts an implementation of a program designed to synchronize two folders: a source and a replica.

The program's objective is to ensure that the replica folder maintains a complete, identical copy of the source folder.

- Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;
- Synchronization should be performed periodically;
- File creation/copying/removal operations should be logged to a file and to the console output;
- Folder paths, synchronization interval and log file path should be provided using the command line arguments;

This synchronization is achieved using only built-in Python libraries.

## How it works

Using the command line, the user sets the following inputs:

- `--source_path`: The path of the source directory, from where the files will be backed up. If the directory does not exist, it will show a message to the user.
- `--replica_path`: The path of the replica directory, where the files from the source directories will be stored. If the directory does not exist, it will show a message to the user.
- `--log_path`: The path of the log file, where all modifications in replica folder folders will be recorded. If the file path does not exist, it will show a message to the user.
- `--sync_time`: The synchronization interval.

From there, the script runs until it is interrupted by the user, recording all modifications of files in the replica folder in the log file, as well as any eventual errors during the process that may stop it from running. The messages are also displayed in the interface.


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

6. Run the program locally by replacing `<SOURCE_FOLDER_PATH>` with the actual source folder path, `<REPLICA_FOLDER_PATH>` with the replica folder path, `<FILE_PATH>` with the log file path, and `<SYNC_INTERVAL>` with the synchronization interval.


```bash
python app --source_path=<SOURCE_FOLDER_PATH> --replica_path=<REPLICA_FOLDER_PATH> --log_path=<FILE_PATH> --sync_time=<SYNC_INTERVAL>
```

To run it as it is in the cloned project, simply execute the following command
```bash
python app  --source_path=data/source --replica_path=data/replica --log_path=logs/log.txt --sync_time=10
```