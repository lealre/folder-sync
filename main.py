import os
import shutil
import hashlib

source_path = 'data/source'
replica_path = 'data/replica'

# Assert folders
if not os.path.isdir(source_path):
    print(f"Source path '{source_path}' does not exist or is not a directory")
    exit()
if not os.path.isdir(replica_path):
    print(f"Replica path '{replica_path}' does not exist or is not a directory")
    exit()

# Get files from directories (Just files)
source_files = [file for file in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, file))]
replica_files = [file for file in os.listdir(replica_path) if os.path.isfile(os.path.join(replica_path, file))]


print(source_files,replica_files)

def compare_two_files(source_file: str, replica_file: str) -> bool:
    with open(source_file, 'rb') as source:
        with open(replica_file, 'rb') as replica:
            if hashlib.md5(source.read()).hexdigest() == hashlib.md5(replica.read()).hexdigest():
                return True
            else: 
                return False

for file in source_files:
    source_file_path = os.path.join(source_path, file)
    replica_file_path = os.path.join(replica_path, file)
    if file in replica_files:
        if compare_two_files(source_file_path, replica_file_path):
            print(f'File {file} already in {replica_path}')
        else:
            shutil.copy2(source_file_path, replica_path)
            print(f'File {file} updated in {replica_path}')
    else:
        # add file to replica folder
        shutil.copy2(source_file_path, replica_path)
        print(f'File {file} added to {replica_path}')
    

for file in replica_files:
    if file not in source_files:
        # remove files from replica
        replica_file_path = os.path.join(replica_path,file)
        os.remove(replica_file_path)
        print(f'File {file} removed from {replica_path}')

        