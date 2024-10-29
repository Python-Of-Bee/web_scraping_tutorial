from selenium import webdriver      # imports
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Import By
from time import sleep
from bs4 import BeautifulSoup


# make a webdriver object   -    chrome driver path for my system -- >    /Users/waqarjoyia/Downloads/chromedriver


# driver = webdriver.Chrome('SELENIUM DIR/chromedriver.exe')
# Đường dẫn đến chromedriver
chrome_service = Service('SELENIUM DIR/chromedriver.exe')
chrome_options = Options()

# Khởi tạo trình duyệt Chrome với service và options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# open some page using get method       - url -- > parameters

driver.get('https://www.google.com/')

search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys("freetuts")

search_bar.submit()

sleep(10)

# driver.get('https://www.facebook.com')

# # driver.page_source

# soup = BeautifulSoup(driver.page_source,'lxml')

# print(soup.prettify())



# close webdriver object

driver.close()

