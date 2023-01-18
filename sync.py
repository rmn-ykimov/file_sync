import os
import argparse
import shutil
import hashlib
import logging
from sched import scheduler

def sync_folders(source, replica, interval, log_file):
    sched = scheduler(time.time, time.sleep)
    sched.enter(interval, 1, sync_folders, (source, replica, interval, log_file))
    logging.basicConfig(filename=log_file,level=logging.INFO)
    # Compare files in source and replica folders
    for file in os.scandir(source):
        source_file = file.path
        replica_file = os.path.join(replica, file.name)

        # If file doesn't exist in replica, copy it
        if not os.path.exists(replica_file):
            shutil.copy2(source_file, replica_file)
            logging.info(f"Copied {source_file} to {replica_file}")
            print(f"Copied {source_file} to {replica_file}")

        # If file exists in replica, check if it's identical
        else:
            source_hash = hashlib.md5(open(source_file, 'rb').read()).hexdigest()
            replica_hash = hashlib.md5(open(replica_file, 'rb').read()).hexdigest()
            
            # If file is different, overwrite replica
            if source_hash != replica_hash:
                shutil.copy2(source_file, replica_file)
                logging.info(f"Overwrote {replica_file}")
                print(f"Overwrote {replica_file}")
    
    # Remove files in replica that don't exist in source
    for file in os.scandir(replica):
        replica_file = file.path
        if not os.path.exists(os.path.join(source, file.name)):
            os.remove(replica_file)
            logging.info(f"Removed {replica_file}")
            print(f"Removed {replica_file}")
    sched.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='Source folder')
