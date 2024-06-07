from sync import FolderSync


source_path = 'data/source'
replica_path = 'data/replica'
log_path = 'logs'
sync_time = 15

sync_folders = FolderSync(source_path=source_path,
                          replica_path=replica_path,
                          log_path=log_path,
                          sync_time=15)
sync_folders.start_sync()   