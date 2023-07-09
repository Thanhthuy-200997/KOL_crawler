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
        f = open(myjson)
        data = json.load(f)
        print(data)
    except ValueError as e:
        return False 
    return True


def get_json_post(post,path):
    if is_json(path) == False:
        with open(path, 'w') as f:
            template = {'post_meta':[{'mediaid':'meta_id','uuid':'is','insta_url':'link post','post_date_local':'post_date','links':'link image','mtime':'time'}]} 
            json_object = json.dumps(template, indent=6)
            f.write(json_object)
            f.close
    else:
        with open(path, 'r+') as f:
            file_data = json.load(f)
            file_data["post_meta"].append(post)
            f.seek(0) 
            json.dump(file_data, f, indent=6,default=str)
            
def save_post(metapost:dict,path_tosave_json):
    for p in metapost['posts']:
        if p['mtime'] >= datetime.datetime(2022, 6, 1, 0, 0, 0):
            get_json_post(p,path_tosave_json)
    return None

def save_image(metapost:dict,path_tosave_img):
    lst_post = metapost['posts']
    for i in range(len(lst_post)):
        if lst_post[i]['mtime'] >= datetime.datetime(2022, 6, 1, 0, 0, 0):
            for link in lst_post[i]['links']:
                img_name = re.findall("//.*/(.*)\?", link)
                FileName = path_tosave_img + ''.join(img_name)
                request_image(link, FileName)
                # print('suscess')
                
            
    

            
    