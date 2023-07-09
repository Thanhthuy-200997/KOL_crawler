import os
import pandas as pd
import datetime
import time
import random
import json
import re
from utils.requests import *

def is_json(myjson):
    assert os.path.isfile(myjson)
    try:
        f = open(myjson, 'r+', encoding='utf8')
        data = json.load(f)
        print(data)
        if data is not None:
            return True
        else:
            return False
    except ValueError as e:
        return False

def append_post(post,path):
    with open(path, 'r+', encoding='utf8') as f:
            file_data = json.load(f)
            file_data["video_meta"].append(post)
            f.seek(0) 
            json.dump(file_data, f, indent=6,default=str, ensure_ascii=False)

def create_json_file(path):
    if is_json(path) == False:
        with open(path, 'w') as f:
            template = {'video_meta':[{'account':'link account','fullname':'name','biography':'bio tiktok','following':'number of following','follower':'number of follower','metapost':'meta info'}]} 
            json_object = json.dumps(template, indent=6)
            f.write(json_object)
            f.close
            
def save_post(metapost:dict,path_tosave_json):
    append_post(metapost,path_tosave_json)
    return None
                
            
    

            
    