from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")

# Đường dẫn tới ChromeDriver
driver_path = "/chromedriver.exe"

# Khởi tạo Service
service = Service(driver_path)

# Khởi tạo WebDriver với Service và các tùy chọn
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.facebook.com/")

findSearchForm = driver.find_element(By.XPATH, '//*[@id="mount_0_0_bd"]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/label/input')
findSearchForm.send_keys('hihi')

driver.close()