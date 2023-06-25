from utils.insta_crawl import *
from utils.GetList_KOL import *
from utils.Parse_metapost_insta import *
import yaml
import sys
sys.path.append('../../')
import config
import re
import logging
import datetime
import time
import random
import pandas as pd

logging.basicConfig(filename="../log/logging.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

yaml_file = open("../config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
img_path = cfg['result']['image']
json_path = cfg['result']['json']
path_KOL = cfg['data']['acc_KOL_insta']

def main():
    try:
        ic = InstaCrawler()
        # lst_KOL_insta = load_list_KOL(path_KOL)
        # for KOL in lst_KOL_insta:
        for KOL in ['junpham']:
            print(f'Get profile {KOL}')
            profile = ic.get_profile(KOL)
            user_meta = ic.get_profile_meta(profile)
            post_meta  = ic.get_posts(profile,user_meta)
            print(f'Write post for {KOL}. Please wait!!!')
            save_post(post_meta,json_path)
            print(f'Successful write post for {KOL}')
            time.sleep(10*60)
            print(f' Save image for {KOL}. Please wait!!!')
            save_image(post_meta,img_path)
            print(f'Successful Save image for {KOL}')
            time.sleep(10*60)
    except Exception as e:
        pass       
if __name__ == "__main__":
    main()
    
    
