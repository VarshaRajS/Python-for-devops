import shutil
import datetime
import os

# source is the file whose backup is required
# destination is the destination where you want to create that backup

def backup_files(source, destination):
    today = datetime.date.today()
    # Construct the full path for the backup file name
    backup_file_name = os.path.join(destination, f"backup_{today}")
    # Create a compressed archive of the source directory
    shutil.make_archive(backup_file_name, 'gztar', source)

source = r"path/to/source/file"
destination = r"path/to/destination"

# Call the function to perform the backup
backup_files(source, destination)

