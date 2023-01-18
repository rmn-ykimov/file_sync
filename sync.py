import os
import argparse
import time
import hashlib

def sync_folders(source, replica, interval, log_file):
    while True:
        # Get list of files in source folder
        source_files = os.listdir(source)
        
        # Compare files in source and replica folders
        for file in source_files:
            source_file = os.path.join(source, file)
            replica_file = os.path.join(replica, file)
            
            # If file doesn't exist in replica, copy it
            if not os.path.exists(replica_file):
                with open(source_file, 'rb') as f_src, open(replica_file, 'wb') as f_dst:
                    f_dst.write(f_src.read())
                log(f"Copied {source_file} to {replica_file}", log_file)
                print(f"Copied {source_file} to {replica_file}")
                
            # If file exists in replica, check if it's identical
            else:
                source_hash = hashlib.md5(open(source_file, 'rb').read()).hexdigest()
                replica_hash = hashlib.md5(open(replica_file, 'rb').read()).hexdigest()
                
                # If file is different, overwrite replica
                if source_hash != replica_hash:
                    with open(source_file, 'rb') as f_src, open(replica_file, 'wb') as f_dst:
                        f_dst.write(f_src.read())
                    log(f"Overwrote {replica_file}", log_file)
                    print(f"Overwrote {replica_file}")
                    
        # Remove files in replica that don't exist in source
        replica_files = os.listdir(replica)
        for file in replica_files:
            if file not in source_files:
                replica_file = os.path.join(replica, file)
                os.remove(replica_file)
                log(f"Removed {replica_file}", log_file)
                print(f"Removed {replica_file}")
                
        time.sleep(interval)
        
def log(message, log_file):
    with open(log_file, 'a') as f:
        f.write(f"{time.ctime()} - {message}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='Source folder')
    parser.add_argument('replica', help='Replica folder')
    parser.add_argument('interval', type=int, help='Synchronization interval in seconds')
    parser.add_argument('log_file', help='Log file path')
    args = parser.parse_args()
    
    sync_folders(args.source, args.replica, args.interval, args.log_file)
