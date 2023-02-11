"""
This module contains the argument parser for the folder syncing utility.
"""
import argparse

def parse_args():
    """
    Parse command line arguments for the folder syncing utility.
    
    Returns:
        argparse.Namespace: An object that contains the parsed arguments.
    """
    parser = argparse.ArgumentParser(description='This script is the entry'
                                     'point to the folder syncing utility.')
    parser.add_argument('--source', '-s', type=str, help='The source folder to'
                        'sync with the replica folder. This folder will be'
                        'used as the source of data to be copied to the'
                        'replica folder.', required=True)
    parser.add_argument('--replica', '-r', type=str, help='The replica folder'
                        'to sync with the source folder. This folder will be'
                        'updated with the data from the source folder.',
                        required=True)
    parser.add_argument('--log-file', '-l', type=str, help='The log file to'
                        'use for logging sync operations. The log file will'
                        'contain information about the changes made during'
                        'each sync operation.', default='/tmp/folder_sync.log')
    parser.add_argument('--dry-run', '-d', action='store_true', help='Run the'
                        'script without making any changes. This is useful for'
                        'testing the script and previewing the changes that'
                        'will be made during a sync operation.')
    return parser.parse_args()
