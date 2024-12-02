# 下載網頁的html檔案

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

class WebDriverManager:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_box_code(self, skin_club_url, box_name):
        url = skin_club_url + box_name + "/odds-history"
        self.driver.get(url)

        # 確保頁面加載完成  
        self.driver.implicitly_wait(60)
        time.sleep(5)

        # 獲取並使用 BeautifulSoup 解析 HTML
        html = self.driver.page_source
        return html

    def quit(self):
        self.driver.quit()

# 測試
if __name__ == "__main__":
    skin_club_url = 'https://skin.club/cases/'
    box_name = 'ct_pistols_farm'
    web_driver_manager = WebDriverManager()
    html_content = web_driver_manager.get_box_code(skin_club_url, box_name)
    print(len(html_content))
    web_driver_manager.quit()