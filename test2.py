from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class AutoCommentFacebook(webdriver.Chrome):
        def __init__(self, driver_path=r"/chromedriver.exe"):
                self.driver_path = driver_path
                os.environ['PATH'] += self.driver_path
                super(AutoCommentFacebook, self).__init__()
                self.implicitly_wait(10)
                self.maximize_window()

        def login(self, fb_mail, fb_pass):

                count = 0
                
                url = 'https://m.facebook.com/'
                self.get(url)

                email = self.find_element(By.NAME, 'email')
                email.send_keys(fb_mail)
                time.sleep(2)
                password = self.find_element(By.NAME, 'pass')
                password.send_keys(fb_pass)
                time.sleep(5)
                login = self.find_element(By.NAME, 'login')
                login.click()
                time.sleep(5)

                keyword = 'theanh28'
                search = 'https://m.facebook.com/search/top/?q=' + keyword
                self.get(search)

                time.sleep(2)

                wait = WebDriverWait(self, 10)

                #get fist post
                find_comment = self.find_element(By.CLASS_NAME, 'story_body_container')
                find_comment.click()
                send_comment = self.find_element(By.NAME, 'comment_text')
                send_comment.click()
                time.sleep(5)
                send_comment.send_keys('hihihi')
                print('Post: ' + str(count + 1) + ' Successfully!')
                time.sleep(2)
                self.back()
                time.sleep(2)
                self.execute_script("window.scrollBy(0,800)","")

                time.sleep(100)

                #get 2nd post
                find_2ndComment = self.find_element(By.CLASS_NAME, 'story_body_container')
                find_2ndComment.click()
                send_2ndComment = self.find_element(By.NAME, 'comment_text')
                send_2ndComment.click()
                send_2ndComment.send_keys('bai thu 2')

                time.sleep(2000)

fb_auto = AutoCommentFacebook(driver_path="/chromedriver.exe")
fb_auto.login('0383369755', 'hochoathaythang')