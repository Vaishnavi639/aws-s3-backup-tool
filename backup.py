import shutil
import datetime
import os

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}.tar.gz")
    print(backup_file_name)
    shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source)

source = "D:\\Python"
destination = "D:\\Python\\backup"
backup_files(source, destination)
