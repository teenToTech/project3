import os
import shutil
from datetime import datetime

source = "data"
destination = "backup"

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_folder = os.path.join(destination, timestamp)

os.makedirs(backup_folder)

for file in os.listdir(source):
    source_file = os.path.join(source, file)
    dest_file = os.path.join(backup_folder, file)
    
    shutil.copy2(source_file, dest_file)

print("Backup completed:", backup_folder)
