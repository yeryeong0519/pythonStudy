import os

path = "/Users/yeryeongseo/desktop"
files = os.listdir(path)
for f in files:
    if(f.find("-") and f,endswidth(".mp3")):
        name = f[0:4]