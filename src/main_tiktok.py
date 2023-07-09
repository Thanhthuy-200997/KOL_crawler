import os
import time
import random
import logging
import sys
import yaml
sys.path.append('../../')
import logging.config
from utils.save_video_tiktok import *
from utils.tiktok_video_crawl import *
from utils.GetList_KOL import *
from utils.Get_html_tiktok import *
from utils.Parse_html_tiktok import *
from utils.tiktok_crawler import *
from utils.save_metapost_tiktok import *



yaml_file = open("../config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
video_path = cfg['result']['video']
json_path = cfg['result']['meta_video']
path_KOL = cfg['data']['acc_KOL_tiktok']
snaptik = cfg['snaptik']

def main():
    # tt = TiktokCrawler()
    # username = 'hoaa.hanassii'
    # user_meta = tt.get_profile_meta(username)
    # print(user_meta)
    
    # API = API_getway()
    # username = 'hoaa.hanassii'
    # fulltext = API.get_html_tiktok(username)
    # parse = parse_html(fulltext)
    # meta = parse.get_profile_meta(username)
    # print('*********************')
    # print(meta)
    # posts = meta['meta_post'].keys()
    # post = list(posts)
    # for p in post[:2]:
    #     sn = Snaptik()
    #     id = re.findall("\d{19}", p)
    #     file_name = '../result/' + ''.join(id) +'.mp4'
    #     print(file_name)
    #     sn.save_video(snaptik,p,file_name)
    lst_KOL_tiktok = load_list_KOL(path_KOL)
    create_json_file(json_path)
    for KOL in lst_KOL_tiktok:
        API = API_getway()
        print(f'start with {KOL}.Please wait!!!!')
        fulltext = API.get_html_tiktok(KOL)
        p = parse_html(fulltext)
        meta_post = p.get_profile_meta(KOL)
        save_post(meta_post,json_path)
        print(f'Successfully save post {KOL}')
        save_video(meta_post,video_path)
        print(f'Successfully save video {KOL}')             
if __name__ == "__main__":
    main()
