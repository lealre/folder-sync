import os

source_path = 'data/source'
replica_path = 'data/replica'

# Assert folders
if not os.path.isdir(source_path):
    print(f'Source path \'{source_path}\' does not exist or is not a directory')
    exit()
if not os.path.isdir(replica_path):
    print(f'Replica path \'{replica_path}\' does not exist or is not a directory')
    exit()

# Get files from directories
source_files = os.listdir(source_path)
replica_files = os.listdir(replica_path)

print(source_files,replica_files)