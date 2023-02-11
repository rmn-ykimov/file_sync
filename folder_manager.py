"""
Module for managing file operations such as copying and removing files.
"""
import os
import shutil

def validate_directories(source_dir: str, replica_dir: str) -> None:
    """
    Validate that both `source_dir` and `replica_dir` are valid directories.

    Args:
        source_dir (str): The path to the source directory.
        replica_dir (str): The path to the replica directory.

    Raises:
        ValueError: If either `source_dir` or `replica_dir` is not a valid
        directory.
    """
    source_dir = os.path.abspath(source_dir)
    replica_dir = os.path.abspath(replica_dir)

    if not os.path.isdir(source_dir):
        raise ValueError("Source directory is not a valid directory.")

    if not os.path.isdir(replica_dir):
        raise ValueError("Replica directory is not a valid directory.")

def copy_file(source_file: str, replica_file: str) -> None:
    """
    Copies the file at `source_file` to `replica_file`.
    
    Args:
        source_file (str): The path to the source file.
        replica_file (str): The path to the replica file.
    
    Raises:
        FileNotFoundError: If the file at `source_file` does not exist.
        OSError: If there is an error copying the file.
    """
    try:
        shutil.copy2(source_file, replica_file)
        print(f"Copied {source_file} to {replica_file}")
    except FileNotFoundError:
        print(f"File {source_file} does not exist.")
    except OSError as error:
        print(f"Error copying {source_file} to {replica_file}: {error}")

def remove_file(replica_file: str) -> None:
    """
    Removes the file at `replica_file`.
    
    Args:
        replica_file (str): The path to the replica file.
    
    Raises:
        FileNotFoundError: If the file at `replica_file` does not exist.
        OSError: If there is an error removing the file.
    """
    try:
        os.remove(replica_file)
    except FileNotFoundError:
        print(f"File {replica_file} does not exist.")
    except OSError as error:
        print(f"Error removing file {replica_file}: {error}")
