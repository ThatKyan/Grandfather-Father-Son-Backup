import os
import shutil
import time
import ctypes

secondsToWait = None

backupDirectory = r"\\192.168.1.115\NetworkStorage\automaticBackups"
toCopyFrom = r"C:\Users\Kyan\Pictures\Roblox"



while True:
    print("Starting backup...")
    os.makedirs(backupDirectory, exist_ok=True)
    if os.path.exists(toCopyFrom):
        for getFile in os.listdir(toCopyFrom):
            getFileDirectory = os.path.join(toCopyFrom, getFile)
            getDestinationDirectory = os.path.join(backupDirectory, getFile)

            if os.path.isdir(getFileDirectory):
                shutil.copytree(getFileDirectory, getDestinationDirectory, dirs_exist_ok= True)
            else:
                shutil.copy2(getFileDirectory, getDestinationDirectory)

    print("Backup done")

    if secondsToWait != None:
        print("Waiting for interval to pass")
        time.sleep(secondsToWait)
    else:
        break



