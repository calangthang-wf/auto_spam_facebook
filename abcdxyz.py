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

                actions = ActionChains(self)
                screen_width = self.execute_script("return window.screen.width;")
                screen_height = self.execute_script("return window.screen.height;")
                print("Kích thước màn hình:")
                print("Chiều ngang:", screen_width)
                print("Chiều dọc:", screen_height)
                self.set_window_size(screen_width, screen_height)

                url = 'https://selenium-python.readthedocs.io/api.html?highlight=back#selenium.webdriver.remote.webdriver.WebDriver.back'
                self.get(url)

                time.sleep(2)
                self.execute_script("window.scrollBy(0,800)","")
                time.sleep(2)
                actions.move_by_offset(100, 100).perform()
                time.sleep(2)
                self.back()
                time.sleep(20)

fb_auto = AutoCommentFacebook(driver_path="/chromedriver.exe")