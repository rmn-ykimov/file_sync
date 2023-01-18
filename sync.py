import os
import argparse
import shutil
import hashlib
import logging
from sched import scheduler

def sync_folders(source, replica, interval, log_file):
    source = os.path.abspath(source)
    replica = os.path.abspath(replica)
    
    if not os.path.isdir(source) or not os.path.isdir(replica):
        raise ValueError("Both source and replica must be valid directories")
        
    if not os.path.exists(replica):
        os.makedirs(replica)
        
    sched = scheduler(time.time, time.sleep)
    sched.enter(interval, 1, sync_folders, (source, replica, interval, log_file))
    logging.basicConfig(filename=log_file,level=logging.INFO, 
                        format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Compare files in source and replica folders
    for file in os.scandir(source):
        source_file = os.path.abspath(file.path)
        replica_file = os.path.join(replica, file.name)
        
        if not os.path.isfile(source_file):
            continue
            
        # If file doesn't exist in replica, copy it
        if not os.path.exists(replica_file):
            shutil.copy2(source_file, replica_file)
            logging.info(f"Copied {os.path.relpath(source_file, source)} to {os.path.relpath(replica_file, replica)}")
        
        # If file exists in replica, check if it's identical
        else:
            source_size = os.path.getsize(source_file)
            replica_size = os.path.getsize(replica_file)
            
            if source_size != replica_size:
                shutil.copy2(source_file, replica_file)
                logging.info(f"Overwrote {os.path.relpath(replica_file, replica)}")
            else:
                with open(source_file, 'rb') as src, open(replica_file, 'rb') as rep:
                    source_hash = hashlib.sha256(src.read()).hexdigest()
                    replica_hash = hashlib.sha256(rep.read()).hexdigest()

                    if source_hash != replica_hash:
                        shutil.copy2(source_file, replica_file)
                        logging.info(f"Overwrote {os.path.relpath(replica_file, replica)}")
                        
    # Remove files in replica that don't exist in source
    for file in os.scandir(replica):
        replica_file = os.path.abspath(file.path)
        
        if not os.path.isfile(replica_file):
            continue
        
        if not os.path.exists(os.path.join(source, file.name)):
            os.remove(replica_file)
