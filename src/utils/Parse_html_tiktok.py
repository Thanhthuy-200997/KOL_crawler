from bs4 import BeautifulSoup
from datetime import datetime
import json

# XPATH = {
#     "fullname": "//h2[contains(@data-e2e, 'user-page-header')"
# }

class parse_html:
    def __init__(self,html_text):
        super(parse_html, self).__init__()
        self.parsed_html = BeautifulSoup(html_text,'html.parser')
        
    def get_name(self)->str:
        full_name = self.parsed_html.body.find('h2', attrs={'data-e2e':'user-subtitle'}).text
        return full_name
    
    def get_following(self)->str:
        number_following = self.parsed_html.body.find('strong', attrs={'data-e2e':'following-count'}).text
        return number_following

    def get_follower(self)->str:
        number_follower = self.parsed_html.body.find('strong', attrs={'data-e2e':'followers-count'}).text
        return number_follower

    def get_bio(self)->str:
        bio = self.parsed_html.body.find('h2', attrs={'data-e2e':'user-bio'}).text
        return bio   
    
    def get_id(self,username)->dict:
        dict_src = {}
        res = self.parsed_html.find_all('script')
        object_json = json.loads(res[10].contents[0])
        dict_posts = object_json['ItemModule']
        for id in dict_posts.keys():
            src = f"https://www.tiktok.com/@{username}/video/{id}"
            created_time = dict_posts[id]['createTime']
            t = int (created_time)
            time = datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
            dict_src[src] = time
        return dict_src

    def get_profile_meta(self,username)->dict:
        profile_meta = {
            "account" : f"https://www.tiktok.com/@{username}?lang=en",
            "fullname": self.get_name(),
            "biography": self.get_bio(),
            "following": self.get_following(),
            "follower": self.get_follower(),
            "meta_post": self.get_id(username)            
        }
        return profile_meta