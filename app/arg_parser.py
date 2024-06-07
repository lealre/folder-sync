import argparse

def parse_args(func):
    def wrapper():
        parser = argparse.ArgumentParser(description='Folder synchronization script')
        parser.add_argument('--source_path', required=True, help='The source folder path.')
        parser.add_argument('--replica_path', required=True, help='The replica folder path.')
        parser.add_argument('--log_path', required=True, help='The log file path.')
        parser.add_argument('--sync_time', required = True, type=int, help='The synchronization interval in seconds.')
        args = parser.parse_args()

        func(args)
    return wrapper