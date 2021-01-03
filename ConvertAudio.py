# tinytag used to read m4a metadata
# mutagen used to write mp3 metadata
from tinytag import TinyTag as tt
from mutagen.easyid3 import EasyID3 as eid3

# will use to recursively search music folder
import os

# just call audio converter
print("Converting... ")
os.system("audioconvert convert .\ .\ --output-format .mp3") # eventually change to all python

for root, dirs, files in os.walk(".", topdown = False):
    for name in files:
        if name.endswith(".m4a"):

            # read metadata of m4a file
            print("Copying metadata for " + name)
            tagM4A = tt.get(name)

            # copy metadata between m4a and mp3
            tempName = name.removesuffix('.m4a')
            mp3file = tempName + '.mp3'
            tagMP3 = eid3(mp3file)

            # print eid3.valid_keys.keys()
            # key tags to copy
            tagMP3['title']       = tagM4A.title
            tagMP3['album']       = tagM4A.album
            #tagMP3['discnumber']  = tagM4A.disc #doesn't work for some reason. might have to do with NULL exception
            tagMP3['artist']      = tagM4A.artist
            tagMP3['albumartist'] = tagM4A.albumartist
            tagMP3['date']        = tagM4A.year
            tagMP3['genre']       = tagM4A.genre
            tagMP3['tracknumber'] = tagM4A.track            
            tagMP3.save()

            print("done.")