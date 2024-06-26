import os
import shutil
import time
from datetime import datetime

DEFAULT_BACKUP_INTERVAL = 10

def backup_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for item in os.listdir(source_folder):
        src_path = os.path.join(source_folder, item)
        dst_path = os.path.join(destination_folder, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dst_path)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Backup completed] at {current_time}\n"
          f"from: {source_folder}\n"
          f"to: {destination_folder}")

def main(source_folder, destination_folder, interval=DEFAULT_BACKUP_INTERVAL):
    while True:
        backup_folder(source_folder, destination_folder)
        time.sleep(interval)

if __name__ == "__main__":
    src_folder = "/Users/a13554/PycharmProjects/backup_folder/test"
    dst_folder = "/Users/a13554/PycharmProjects/backup_folder/test_backup"
    backup_interval = 2  # Time in seconds between backups
    main(src_folder, dst_folder, backup_interval)
