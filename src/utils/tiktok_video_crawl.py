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
from utils.requests import *
import sys
import yaml
sys.path.append('../../')

yaml_file = open("../config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
snaptik = cfg['snaptik']


XPATH = {
    "button_download": "//button[contains(@type,'submit')]",
    "path_video": "//a[contains(@data-event,'cdn_snaptik') or contains(@data-event,'download_albumPhoto_mp4Render')]"
    # $x("//a[@data-event = 'download_albumPhoto_mp4Render' or @data-event = 'cdn_snaptik']")
 }


class Snaptik:
    def __init__(self, headless: bool = True) -> None:
        """
        Args:
            headless (bool, optional): open webdriver in headless mode or not. Defaults to True.
        """

        super(Snaptik, self).__init__()

        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("start-maximized")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument('ignore-certificate-errors')
        else:
            chrome_options = None
        # self.driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe', options=chrome_options)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='99.0.4844.51').install()), options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def sleep(self) -> None:
        time.sleep(random.randint(10, 60))
        
    def get_snaptik(self,url_snaptik):
        url_snaptik = snaptik
        self.driver.get(url_snaptik)
    
    def save_video(self,url_snaptik,src,dir_des):
        self.get_snaptik(url_snaptik)
        # lst_src = []
        input_text_fname = self.driver.find_element(By.ID, 'url')
        input_text_fname.send_keys(src)
        actions_ = ActionChains(self.driver)
        button = self.driver.find_element(By.XPATH, XPATH['button_download'])
        actions_.move_to_element(button).click().perform()
        time.sleep(random.randint(10, 15))
        posts = self.driver.find_element(By.XPATH, XPATH["path_video"])
        post = posts.get_attribute('href')
        print('---------------------')
        print(post)
        request_video(post,dir_des)
        # lst_src.append(post)
        self.driver.close()
        return post
        
        
        
        
    

    