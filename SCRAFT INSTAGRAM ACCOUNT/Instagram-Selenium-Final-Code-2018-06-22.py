from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from xlsxwriter import Workbook
import os
import requests
import shutil
import sys

class App:
    def __init__(self, username='beesupper', password='P@ssword1', target_username='tuilatranthanhday',
                 path='SCRAFT INSTAGRAM ACCOUNT/Images'): #Change this to your Instagram details and desired images path
        
        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path

        self.chrome_service = Service('SCRAFT INSTAGRAM ACCOUNT/chromedriver.exe')
        self.chrome_options = Options()
        self.chrome_options.add_argument("--start-maximized")  # Mở cửa sổ ở chế độ tối đa
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options) #Change this to your ChromeDriver path.

        self.error = False
        self.main_url = 'https://www.instagram.com/accounts/emailsignup/'
        self.home_url = 'https://www.instagram.com/'
        self.all_images = []
        self.driver.get(self.main_url)

        sleep(2)
        self.log_in()
        sleep(4)
        if self.error is False:
            # self.close_dialog_box()
            self.open_target_profile()
        if self.error is False:
            self.scroll_down()
        if self.error is False:
            if not os.path.exists(path):
                os.mkdir(path)
            self.downloading_images()
        # sleep(3)
        self.driver.close()

    def write_captions_to_excel_file(self, images, caption_path):
        print('writing to excel')
        workbook = Workbook(os.path.join(caption_path, 'captions.xlsx'))
        worksheet = workbook.add_worksheet()
        row = 0
        worksheet.write(row, 0, 'Image name')       # 3 --> row number, column number, value
        worksheet.write(row, 1, 'Caption')
        row += 1
        for index, image in enumerate(images):
            filename = 'image_' + str(index) + '.jpg'
            try:
                caption = image['alt']
            except KeyError:
                caption = 'No caption exists'
            worksheet.write(row, 0, filename)
            worksheet.write(row, 1, caption)
            row += 1
        workbook.close()

    def download_captions(self, images):
        captions_folder_path = os.path.join(self.path, 'captions')
        if not os.path.exists(captions_folder_path):
            os.mkdir(captions_folder_path)
        self.write_captions_to_excel_file(images, captions_folder_path)
        '''for index, image in enumerate(images):
            try:
                caption = image['alt']
            except KeyError:
                caption = 'No caption exists for this image'
            file_name = 'caption_' + str(index) + '.txt'
            file_path = os.path.join(captions_folder_path, file_name)
            link = image['src']
            with open(file_path, 'wb') as file:
                file.write(str('link:' + str(link) + '\n' + 'caption:' + caption).encode())'''


    def downloading_images(self):

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')

        # Lọc các thẻ img có src bắt đầu bằng "https://"
        https_images = [img for img in all_images if img.get('src', '').startswith('https://')]
        # print(https_images)
        # print(len(https_images))
        # sys.exit(0)
        for index, image in enumerate(https_images, start=0):
            
            # Co loi tai day, ly do link anh da bi ma hoa

            print(index)
            print(image)
            sys.exit(0)
            file_name = 'image_' + str(index) + '.jpg'
            image_path = os.path.join(self.path, file_name) # image_path = self.path + '/' + file_name| SCRAFT INSTAGRAM ACCOUNT/Images/image_1
            link = image['src']
            print('Downloading image', index)
            response = requests.get(link, stream=True)

            try:
                if response.status_code == 200:
                    with open(image_path, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=1024):
                            file.write(chunk)
            except Exception as e:
                print(e)
                print('Could not download image number ', index)
                print('Image link -->', link)


        sys.exit(0)



        self.all_images = list(set(self.all_images))
        self.download_captions(self.all_images)
        print('Length of all images', len(self.all_images))
        for index, image in enumerate(self.all_images):
            filename = 'image_' + str(index) + '.jpg'
            image_path = os.path.join(self.path, filename)
            link = image['src']
            print('Downloading image', index)
            response = requests.get(link, stream=True)
            try:
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)  # source -  destination
            except Exception as e:
                print(e)
                print('Could not download image number ', index)
                print('Image link -->', link)

    def scroll_down(self):
        try:
            try:
                no_of_posts_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@class='x5n08af x1s688f']"))
                )
                no_of_posts = no_of_posts_element.text
            except Exception as e:
                print("Không thể tìm thấy số bài post:", e)

            # no_of_posts = no_of_posts.replace(' posts', '')
            no_of_posts = str(no_of_posts).replace(',', '')  # 15,483 --> 15483
            self.no_of_posts = int(no_of_posts)
            if self.no_of_posts > 12:
                # no_of_scrolls = int(self.no_of_posts/12) + 3
                no_of_scrolls = 1
                try:
                    for value in range(no_of_scrolls):
                        soup = BeautifulSoup(self.driver.page_source, 'lxml')
                        for image in soup.find_all('img'):
                            self.all_images.append(image)
                        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                        sleep(2)
                except Exception as e:
                    self.error = True
                    print(e)
                    print('Some error occurred while trying to scroll down')
            sleep(2)
           
        except Exception:
            print('Could not find no of posts while trying to scroll down')
            self.error = True


    def open_target_profile(self):
        try:
            try:
                search_bar = self.driver.find_element(By.LINK_TEXT, 'Search')
                # search_bar = self.driver.find_element(By.XPATH, '//span[@aria-describedby=":r21:"]')
                search_bar.click()
                sleep(3)
            except:
                self.error = True
                print('Khong tim thay nut Search')
            # input_search = self.driver.find_element(By.XPATH, '//input[@aria-label="Search input"]')
            
            try:
                input_search = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search input"]'))
                )
                input_search.send_keys(self.target_username)  # Gửi từ khóa tìm kiếm
            except TimeoutException:
                print("Unable to find input search box: Timeout after 10 seconds.")
            except Exception as e:
                print("Some other exception occurred:", e)

            target_profile_url = self.home_url + self.target_username + '/'
            self.driver.get(target_profile_url)

        except Exception:
            self.error = True
            print('Could not find search bar')

    def close_dialog_box(self):
        # reload page
        sleep(2)
        self.driver.get(self.driver.current_url)
        sleep(3)

        try:
            sleep(3)
            not_now_btn = self.driver.find_element_by_xpath('//*[text()="Not Now"]')
            sleep(3)

            not_now_btn.click()
            sleep(1)
        except Exception:
            pass


    def close_settings_window_if_there(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as e:
            pass

    def log_in(self, ):
        try:
            # log_in_button = self.driver.find_element(By.LINK_TEXT, 'Log in')
            log_in_button = self.driver.find_element(By.XPATH, '//main[@role="main"]//span[@class="_ap3a _aaco _aacw _aad0 _aad7"]')
            log_in_button.click()
            sleep(1)
           
        except Exception:
            self.error = True
            print('Unable to find login button')
        else:
            try:
                user_name_input = self.driver.find_element(By.XPATH, '//input[@aria-label="Phone number, username, or email"]')
                user_name_input.send_keys(self.username)
                sleep(1)

                password_input = self.driver.find_element(By.XPATH, '//input[@aria-label="Password"]')
                password_input.send_keys(self.password)
                sleep(1)
                
                # user_name_input.submit()
                password_input.submit()
                sleep(1)

                # self.close_settings_window_if_there()
            except Exception:
                print('Some exception occurred while trying to find username or password field')
                self.error = True



if __name__ == '__main__':
    app = App()