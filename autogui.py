from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyautogui

class AutoCommentFacebook(webdriver.Chrome):
        def __init__(self, driver_path=r"/chromedriver.exe"):
                self.driver_path = driver_path
                os.environ['PATH'] += self.driver_path
                super(AutoCommentFacebook, self).__init__()
                self.implicitly_wait(10)
                self.maximize_window()

        def login(self, fb_mail, fb_pass):

            url = 'https://m.facebook.com/'
            self.get(url)

            #login
            email = self.find_element(By.NAME, 'email')
            email.send_keys(fb_mail)
            time.sleep(2)
            password = self.find_element(By.NAME, 'pass')
            password.send_keys(fb_pass)
            time.sleep(5)
            login = self.find_element(By.NAME, 'login')
            login.click()
            time.sleep(5)

            keyword = 'beatvn'
            search = 'https://m.facebook.com/search/top/?q=' + keyword
            self.get(search)
            time.sleep(2)

            self.execute_script("window.scrollBy(0,800)","")
            # find everything
            screen_width, screen_height = pyautogui.size()
            pyautogui.moveTo(100, 100)
            print('set df')
            time.sleep(5)
            while True:
                    x, y = pyautogui.position()
                    new_x = x + 700
                    new_y = y + 650
                    print("done")

                    if new_x >= screen_width or new_y >= screen_height:
                        new_x = 0
                        new_y = 0

                    pyautogui.moveTo(new_x, new_y, duration=0.25)
                
                    time.sleep(100)   


fb_auto = AutoCommentFacebook(driver_path="/chromedriver.exe")
fb_auto.login('0383369755', 'hochoathaythang')