from selenium import webdriver      # imports
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Import By
from time import sleep
from bs4 import BeautifulSoup

# Đường dẫn đến chromedriver
chrome_service = Service('SELENIUM DIR/chromedriver.exe')
chrome_options = Options()

# Khởi tạo trình duyệt Chrome với service và options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)



# open instagram.com -- > url --> https://www.instagram.com

driver.get('https://www.instagram.com/accounts/emailsignup/')

sleep(5)

login_button = driver.find_element(By.LINK_TEXT, 'Log in')

login_button.click()

sleep(5)


driver.close()