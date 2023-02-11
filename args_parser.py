"""
This module contains the argument parser for the folder syncing utility.
"""
import argparse

def parse_args():
    """
    Parse command line arguments for folder syncing utility.
    """
    parser = argparse.ArgumentParser(description='This script is the entry'
                                     'point to the folder syncing utility.')
    parser.add_argument('--source', '-s', type=str, help='The source folder to sync', required=True)
    parser.add_argument('--replica', '-r', type=str, help='The replica folder to sync', required=True)
    parser.add_argument('--log_file', '-l', type=str, help='The log file to use', required=True)
    parser.add_argument('--dry-run', '-d', action='store_true', help='Run the script without making any changes')
    return parser.parse_args()
