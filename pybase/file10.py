import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "/" + f
        if os.path.isdir(fullpath)
        print(f)
        