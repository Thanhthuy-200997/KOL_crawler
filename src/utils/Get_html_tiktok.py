import requests
import urllib
from requests_ip_rotator import ApiGateway,EXTRA_REGIONS
import re
import sys
import yaml
sys.path.append('../../')


yaml_file = open("../config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
Gateway = cfg['Gateway']
access_key_id = cfg['AWS_infor']['access_key_id']
access_key_secret = cfg['AWS_infor']['access_key_secret']


# def get_video_url(xgwrapper:str,username: str)->str:
#     id = re.findall("xgwrapper-2-(.*)", xgwrapper)
#     video_url = f"https://www.tiktok.com/@{username}/video/{id}"
#     return video_url

class API_getway:
    def __init__(self):
        super(API_getway, self).__init__()
        self.GateWay = ApiGateway(Gateway, access_key_id=access_key_id, access_key_secret=access_key_secret)
    
    def get_html_tiktok(self,username):
        gateway = self.GateWay
        gateway.start(force=True)
        session = requests.Session()
        session.mount(Gateway, gateway)
        profile = f"https://www.tiktok.com/@{username}?lang=en"
        response = session.get(profile, params={"theme": "light"})
        print(response.status_code)
        html_text = response.text
        # print(response.text)
        gateway.shutdown()
        return html_text
                
            
    

            
    