from sync import FolderSync
from arg_parser import parse_args

@parse_args
def main(args):
    FolderSync(
        source_path=args.source_path,
        replica_path=args.replica_path,
        log_path=args.log_path,
        sync_time=args.sync_time
    ).start_sync()

main()