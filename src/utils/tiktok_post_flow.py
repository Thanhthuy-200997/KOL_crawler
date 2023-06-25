from utils.tiktok_crawl import *
from pathlib import Path
import time
import random
from utils.requests_image import *
import re
# check_path = './data/checked.txt'
# check_path = './data/unchecked.txt'
# valid_path = './data/valid_user.txt'

# valid = read_username(valid_path)


def tiktok_post_flow(user_meta: dict):
    username = user_meta['username']
    tt = TiktokCrawler()
    #open browser:
    tt.get_profile(username)

    #get list post:
    posts = tt.get_list_post()

    #get each post meta:
    if 'posts' not in user_meta:
        user_meta['posts'] = []

    for idx, post in enumerate(posts):
        post_meta = tt.get_post_meta(post, username)
        if idx == 0:
            user_meta['last_upload'] = post_meta['created_at']            
        #append to user post:
        user_meta['posts'].append(post_meta)
        time.sleep(random.randint(3, 5))

    return user_meta

def save_image(metapost:dict,path_tosave_img):
    lst_post = metapost['lst_img']
    for i in range(len(lst_post)):
        if lst_post[i]['mtime'] >= datetime.datetime(2022, 6, 1, 0, 0, 0):
            for link in lst_post[i]['links']:
                img_name = re.findall("//.*/(.*)\?", link)
                FileName = path_tosave_img + ''.join(img_name)
                request_image(link, FileName)
                # print('suscess')