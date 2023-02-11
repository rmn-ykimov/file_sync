"""
This module implements a folder syncing utility.
"""
import folder_manager
import hash_manager
import log_manager


def sync_folders(source, replica, log_file):
    """
    Synchronize the source and replica folders.
    """
    log_manager.initialize_logger(log_file)
    folder_manager.validate_directories(source, replica)
    compare_and_update_files(source, replica)
    delete_obsolete_files(source, replica)
