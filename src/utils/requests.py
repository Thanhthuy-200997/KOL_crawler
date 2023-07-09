import yaml
import sys
sys.path.append('../../')
import config
import requests
import json

def request_image(link, filename):

    payload={}
    headers = {
      'Cookie': '_cfuvid=Q1a0Cvoh6_5F4cbZcwlq_sdw93DFYHzAR5TsQSAtUtg-1667363759153-0-604800000'
    }

    res = requests.request("GET", link, headers=headers, data=payload)
    
    if res.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(res.content)
    else:
      pass
    return None
  
def request_video(link,filename):
  resp = requests.get(link)
  with open(filename, "wb") as f:
    f.write(resp.content)
  return None