import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from .tiktok_utils import *
from utils.Parse_metapost_tiktok import *

# logger = logging.getLogger("crawl")


XPATH = {
    "username": "//h1[@data-e2e='user-subtitle']",
    "likes": "//strong[@title='Likes']",
    "user_bio": "//h2[@data-e2e = 'user-bio']",
    'list_posts': "//div[contains(@data-e2e,'user-post-item')]/*/*[contains(@class,'DivWrapper')]/a",
    'id': "//div[contains(@id,'xgwrapper')]",
    'img_src': "//img[@mode = '1']",
    'elem_src': "//div[contains(@data-e2e,'user-post-item')]/*/*[contains(@class,tiktok-x6f6za-DivContainer-StyledDivContainerV2.eq741c50)]",
    'button_down': "//button[contains(@data-e2e,'arrow-right')]"
 }


class TiktokCrawler:
    def __init__(self, headless: bool = False) -> None:
        """
        Args:
            headless (bool, optional): open webdriver in headless mode or not. Defaults to True.
        """

        super(TiktokCrawler, self).__init__()

        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("start-maximized")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument('ignore-certificate-errors')
        else:
            chrome_options = None
        self.driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe', options=chrome_options)
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='99.0.4844.51').install()), options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def sleep(self) -> None:
        time.sleep(random.randint(10, 60))

    def get_list_post(self):
        posts = self. driver.find_elements(By.XPATH, XPATH['list_posts'])
        posts = [post.get_attribute('href') for post in posts]
        return posts
    def get_list_img(self):
        lst_img = self. driver.find_elements(By.XPATH, XPATH['img_src'])
        print(lst_img)
        _img = [img.get_attribute('src') for img in lst_img]
        return _img
    
    
    def get_id(self)->list:
        actions_ = ActionChains(self.driver)
        self.driver.refresh()
        actions_.move_by_offset(7,7)
        lst_elem = self.driver.find_elements(By.XPATH, XPATH['elem_src'])
        lst_id = []
        count = 0
        actions_.move_by_offset(-7,-7)
        actions_.move_to_element(lst_elem[0]).double_click().move_by_offset(5,5).perform()
        time.sleep(random.randint(10, 15))
        # actions.move_to_element_with_offset(lst_elem[0],5,5).perform()
        id = self.driver.find_element(By.XPATH, XPATH['id']).get_attribute("id")
        print("**************")
        print(id)
        lst_id.append(id)
        while(count<=(len(lst_elem))):
            actions = ActionChains(self.driver)
            button = self.driver.find_element(By.XPATH, XPATH['button_down'])
            actions.move_to_element(button).double_click().perform()            
            time.sleep(10)
            idx = self.driver.find_element(By.XPATH, XPATH['id']).get_attribute("id")
            print("============")
            print(idx)
            lst_id.append(idx)
            count = count + 1
            if count % 5 == 0:
                actions.move_by_offset(5,5)
            else:
                pass
        self.driver.close()
        return lst_id

    def get_profile_num_likes(self) -> str:
        ele = self.driver.find_element(By.XPATH, XPATH["likes"])
        likes = ele.text
        likes = process_number(likes)
        return likes

    def get_profile_bio(self) -> str:
        actions = ActionChains(self.driver)
        actions.move_by_offset(5,5)
        ele = self.driver.find_element(By.XPATH, XPATH["user_bio"])
        bio = ele.text

        return bio

    def get_profile_full_name(self) -> str:
        actions = ActionChains(self.driver)
        actions.move_by_offset(5,5)
        ele = self.driver.find_element(By.XPATH, XPATH["username"])
        username = ele.text
        return username

    def get_profile(self, username: str) -> str:
        url = f"https://www.tiktok.com/@{username}?lang=en"
        self.driver.get(url)

    def get_profile_meta(self, username: str) -> dict[str, list]:
        self.get_profile(username)

        profile_meta = {
            "id": 0,
            "username": username,
            "url": f"https://www.tiktok.com/@{username}?lang=en",
            "biography": self.get_profile_bio(),
            "full_name": self.get_profile_full_name(),
            "list_post": self.get_list_post(),
            "lst_img": self.get_list_img(),
            "lst_id": self.get_id()            
        }

        return profile_meta
    
    def get_post_meta(self, link_post, username):
        id = int(link_post.split('/')[-1])
        link_post+='?lang=en'
        # print(link_post)
        ##open browser:
        self.driver.get(link_post)
        time.sleep(10)
        #get video source:
        video_source = self.driver.find_element(By.XPATH, XPATH['video_source']).get_attribute('src')
        names = cut_frame(username, id, video_source)

        #get date post:
        date = self.driver.find_element(By.XPATH, XPATH['created_at']).get_attribute("innerHTML")
        # print(date)
        date = process_time(date)

        #get like count:
        like_count = process_number(self.driver.find_element(By.XPATH, XPATH['likes_count']).text)

        post_meta = {'url': link_post, 'created_at': date, 'like-count': like_count, 'paths': names}

        return post_meta