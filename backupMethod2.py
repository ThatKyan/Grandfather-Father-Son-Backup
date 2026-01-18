from datetime import datetime, timezone, timedelta
import shutil
import os
import time
import math


TIMEZONE = timezone.utc
BACKUP_SOURCE = r"C:\Users\Kyan\Pictures"
BACKUP_DESTINATION = r"Z:\replicatedFile"

NOTIFY_EMAIL = None

current_time = datetime.now(TIMEZONE)
time_since_to_backup = current_time - timedelta(days=1)

day_in_week = current_time.weekday() # Handles each day in week backup
week_in_month = round(current_time.day /7)
month_in_year = current_time.month

def filesFilter(directory, filesArray):
    filesToIgnore = []
    for file in filesArray:
        #print(directory + "/" + file)
        this_file_path = directory + "/" + file
        file_stats = os.stat(this_file_path)

        
        file_seconds_created = file_stats.st_birthtime


        utc_time_created = datetime.fromtimestamp(file_seconds_created, TIMEZONE)

        if utc_time_created > time_since_to_backup:
            print("time since yesterday " + str(time_since_to_backup))
            print("created time " + str(utc_time_created))
            print("this file is from today || " + str(utc_time_created - time_since_to_backup))
        else:
            filesToIgnore.append(file)

     #   print(os.stat(this_file_path))

        print(file)        

    return filesToIgnore



def backup(timesincetobackup:datetime, backup_folder_name:str):

    try:
        backup_folder = BACKUP_DESTINATION + backup_folder_name


        if os.path.isdir(backup_folder):
            print("there is already folder, removing")
            shutil.rmtree(backup_folder)

        shutil.copytree(src=BACKUP_SOURCE, dst=backup_folder, ignore = filesFilter)
        print("Backup successful!")
    except Exception:
        print("Backup failed!")



if current_time.day == 30:
    # grand father
    print("Doing grandfather backup!")
    backup(timedelta(days=30), "Grandfather" + str(month_in_year))
elif day_in_week == 7:
    # father
    print("Doing father backup!")
    backup(timedelta(days=7), "Father" + str(week_in_month))
else:
    # son
    print("Doing son backup!")
    backup(timedelta(days=1), "Son" + str(day_in_week))



backup(timedelta(days=7), "Father" + str(week_in_month))
