import os
import time
from datetime import datetime

# Function to update metadata of a file
def update_file_metadata(file_path, timestamp):
    # Convert datetime to seconds since the epoch
    timestamp_seconds = time.mktime(timestamp.timetuple())
    
    # Update file modification and access times
    os.utime(file_path, (timestamp_seconds, timestamp_seconds))

# Function to process all files in the current directory
def update_all_files_metadata(directory, new_datetime):
    # Convert datetime to a datetime object
    if isinstance(new_datetime, str):
        new_datetime = datetime.strptime(new_datetime, "%Y-%m-%d %H:%M:%S")
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            print(f"Updating metadata for file: {filename}")
            update_file_metadata(file_path, new_datetime)
            print(f"Metadata updated for: {file_path}")

if __name__ == '__main__':
    current_directory = os.getcwd()
    # Specify the new datetime for metadata (format: "YYYY-MM-DD HH:MM:SS")
    new_datetime_str = "2024-07-23 00:00:00"
    update_all_files_metadata(current_directory, new_datetime_str)
