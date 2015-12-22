import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

def recognizeThis():
    # load config from a JSON file (or anything outputting a python dictionary)
    with open("dejavu.cnf.SAMPLE") as f:
        config = json.load(f)
        # create a Dejavu instance
        djv = Dejavu(config)
        # Recognize audio from a file
        song = djv.recognize(FileRecognizer, "sample.mp3")
        name = song['song_name']
        # Get artist and track name
        char = name.find("-",0,len(name))
        artist = name[:char].rstrip()
        title = name[char+1:].lstrip()
        result=[artist,title]
    return result
