import os
import time
import random
import logging
import sys
import yaml
sys.path.append('../../')
import logging.config
from utils.tiktok_video_crawl import *
from utils.GetList_KOL import *
from utils.Get_html_tiktok import *
from utils.Parse_html_tiktok import *

def save_video(metapost:dict,path_tosave_video):
    # API = API_getway()
    # fulltext = API.get_html_tiktok(username)
    # p = parse_html(fulltext)
    # profile_meta = p.get_profile_meta(username)
    posts = metapost['meta_post'].keys()
    for p in posts:
        sn = Snaptik()
        id = re.findall("\d{19}", p)
        file_name = path_tosave_video + ''.join(id) +'.mp4'
        sn.save_video(snaptik,p,file_name)
    return None
    
    
    