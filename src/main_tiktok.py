import os
import time
import random
import logging
import sys
import yaml
sys.path.append('../../')
import logging.config
from utils.tiktok_post_flow import *
from utils.tiktok_crawl import *
from utils.GetList_KOL import *
from selenium.webdriver.chrome.options import Options



yaml_file = open("../config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
# img_path = cfg['result']['image']
# json_path = cfg['result']['json']
path_KOL = cfg['data']['acc_KOL_tiktok']

def main():
    tt = TiktokCrawler()
    username = 'hoaa.hanassii'
    # url = "https://www.tiktok.com/@hoaa.hanassii?lang=en"
    user_meta = tt.get_profile_meta(username)
    # user_meta = tiktok_post_flow(user_meta)
    print(user_meta)
    
    
if __name__ == "__main__":
    main()
