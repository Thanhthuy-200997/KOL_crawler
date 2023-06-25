import os
import pandas as pd
import datetime
import time
import random
import json
import re
from utils.requests_image import *

def get_video_url(xgwrapper:str,username: str)->str:
    id = re.findall("xgwrapper-2-(.*)", xgwrapper)
    video_url = f"https://www.tiktok.com/@{username}/video/{id}"
    return video_url
                
            
    

            
    