"""
Module for handling log messages and initializing the logger
"""
import logging

def initialize_logger(log_file):
    """
    Initializes the logger object.
    
    Args:
        log_file (str): The file name to store log information.
    
    Returns:
        logger: The logger instance.
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
    return logger


def log_message(message: str) -> None:
    """
    Logs a message with the logger instance.
    
    Args:
        message (str): The message to be logged.
    """
    logger = logging.getLogger(__name__)
    logger.info(message)
