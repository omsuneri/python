# using built in module os to list the contents of a directory in python 
import os 
directory_path = "/usr/bin"
contents = os.listdir(directory_path)
for items in contents:
    print(items)
