from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
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

                keyword = 'beatvn'
                search = 'https://m.facebook.com/search/top/?q=' + keyword
                self.get(search)

                time.sleep(2)

                action = ActionBuilder(webdriver)

                screen_width = self.execute_script("return window.screen.width;")
                screen_height = self.execute_script("return window.screen.height;")
                print("Kích thước màn hình:")
                print("Chiều ngang:", screen_width)
                print("Chiều dọc:", screen_height)
                self.set_window_size(screen_width, screen_height)

                self.execute_script("window.scrollBy(0,800)","")

                #get fist post
                action.pointer_action.move_to_location(700, 650)
                action.pointer_action.click()

                find_comment = self.find_element(By.CLASS_NAME, '_15kq _77li _l-a')
                find_comment.click()
                send_comment = self.find_element(By.XPATH, '//*[@id="composerInput"]')
                send_comment.click()
                send_comment.send_keys('hihihiihi')
                print('Post: ' + str(count + 1) + ' Successfully!')
                time.sleep(2)

                #get 2nd post
                find_2ndComment = self.find_element(By.XPATH, '//*[@id="feedback_inline_pfbid02QhZckmENPg6UDdxGnKVeurUXp5yZwpp3i3nG84SMPADRgZcn4LGUwz4j2A9i76ZMl"]/div[2]/div[2]/a')
                find_2ndComment.click()
                send_2ndComment = self.find_element(By.XPATH, '//*[@id="composerInput"]')
                send_2ndComment.click()
                send_2ndComment.send_keys('hihihhihi')

                time.sleep(2000)

fb_auto = AutoCommentFacebook(driver_path="/chromedriver.exe")
fb_auto.login('0383369755', 'hochoathaythang')