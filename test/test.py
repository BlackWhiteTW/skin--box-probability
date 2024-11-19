# 測試程式

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# 使用 webdriver_manager 來自動下載和安裝 ChromeDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 如果你不需要看到瀏覽器，可以使用 headless 模式

# 初始化 WebDriver
driver = webdriver.Chrome(service=service, options=options)

# 將網頁語言改成英文
url = "https://skin.club/en/cases/znorux_case/odds-history"
driver.get(url)

# 設定 cookie 來自動同意
cookie = {
    'name': 'cookie_consent',
    'value': 'true'
}
driver.add_cookie(cookie)

# 重新加載頁面以應用 cookie
driver.get(url)

# 確保頁面加載完成
driver.implicitly_wait(10)
time.sleep(5)  # 增加等待時間，確保頁面完全加載

# 獲取渲染後的 HTML 內容
html = driver.page_source

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')

# 將渲染後的 HTML 內容重新排版並儲存到文件中
with open('test/test.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# 擷取包含 class="row" 的所有元素
rows = soup.find_all('div', class_='row')

# 進一步解析每個 row 中的內容
for row in rows:
    item_cell = row.find('div', class_='cell item-cell')
    price_cell = row.find('div', class_='cell price-cell')
    range_cell = row.find('div', class_='cell range-cell')
    odds_cell = row.find('div', class_='cell odds-cell')
    
    if item_cell and price_cell and range_cell and odds_cell:
        weapon_name = item_cell.find('span', class_='weapon-name').text
        weapon_finish = item_cell.find('span', class_='weapon-finish').text
        weapon_quality = item_cell.find('span', class_='quality').text
        price = price_cell.text.strip()
        odds_range = range_cell.text.strip()
        odds = odds_cell.text.strip()
        
        print(f"Weapon: {weapon_name} | {weapon_finish} {weapon_quality}")
        print(f"Price: {price}")
        print(f"Range: {odds_range}")
        print(f"Odds: {odds}")
        print("-" * 40)

# 關閉瀏覽器
driver.quit()
