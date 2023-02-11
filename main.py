"""
This script is the entry point to the folder syncing utility.
"""
import args_parser
from sync import sync_folders

if __name__ == "__main__":
    args = args_parser.parse_args()
    source = args.source
    replica = args.replica
    log_file = args.log_file
    sync_folders(source, replica, log_file)
