"""
Module for comparing file hashes

This module contains a function for comparing the hash values of two files.
"""
import hashlib
import log_manager


logger = log_manager.initialize_logger('log.txt')
log_message = log_manager.log_message

def compare_file_hashes(source_file: str, replica_file: str) -> bool:
    """
    Compare the hashes of two files.

    Args:
        source_file (str): Path to the source file.
        replica_file (str): Path to the replica file.

    Returns:
        bool: True if the files have the same hash, False otherwise.

    Raises:
        FileNotFoundError: If either `source_file` or `replica_file` does not
        exist.
    """
    try:
        with open(source_file, 'rb') as src, open(replica_file, 'rb') as rep:
            source_hash = hashlib.sha256(src.read()).hexdigest()
            replica_hash = hashlib.sha256(rep.read()).hexdigest()
            return source_hash == replica_hash
    except FileNotFoundError as error:
        log_message(f"Error: One of the files could not be found: {error}")
        return False
