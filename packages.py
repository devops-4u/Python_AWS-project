import os
import shutil  #This library is used to acces linux shell
total, free, used= shutil.disk_usage("/")
print(f"Total disk space: {total // (2**30)}GB")
print(f"free disk space: {free // (2**30)}GB")
print(f"Used disk space: {used // (2**30)}GB")
#print(os.getcwd())