# 測試程式

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import sqlite3
import time

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# 初始化 WebDriver
driver = webdriver.Chrome(service=service, options=options)
url = "https://skin.club/en/cases/znorux_case/odds-history"
driver.get(url)

# 確保頁面加載完成
driver.implicitly_wait(10)
time.sleep(5)  # 增加等待時間

# 獲取並使用 BeautifulSoup 解析 HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# HTML 排版並儲存到文件中
with open('test/test.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# 提取包含 class="row" 的所有元素
rows = soup.find_all('div', class_='row')
print(len(rows))

# 連接到 SQLite 資料庫
conn = sqlite3.connect('test.db')
c = conn.cursor()

# 建立表格
c.execute('''CREATE TABLE IF NOT EXISTS odds_history
            (weapon_name TEXT, weapon_finish TEXT, weapon_quality TEXT, price TEXT, odds_range TEXT, odds TEXT)''')

# 進一步解析每個 row 中的內容
for row in rows:
    
    item_cell = row.find('div', class_='cell item-cell')
    price_cell = row.find('div', class_='cell price-cell ellipsis')
    range_cell = row.find('div', class_='cell range-cell ellipsis')
    odds_cell = row.find('div', class_='cell odds-cell ellipsis')
    
    # 列印出每個 cell 的內容 (測試用)
    # print(item_cell, "\n", price_cell, "\n", range_cell, "\n", odds_cell)
    
    # 判斷是否找到了所有的 cell
    if item_cell and price_cell and range_cell and odds_cell:
        weapon_name = item_cell.find('span', class_='weapon-name').text
        weapon_finish = item_cell.find('span', class_='weapon-finish').text
        weapon_quality = item_cell.find('span', class_='quality').text
        price = price_cell.text.strip()
        odds_range = range_cell.text.strip()
        odds = odds_cell.text.strip()
        
        # 列印出這次找到的的內容
        print("-" * 40)
        print(f"Weapon: {weapon_name} | {weapon_finish} {weapon_quality}")
        print(f"Price: {price}")
        print(f"Range: {odds_range}")
        print(f"Odds: {odds}")
        
        # 將資料插入資料庫
        c.execute("INSERT INTO odds_history (weapon_name, weapon_finish, weapon_quality, price, odds_range, odds) VALUES (?, ?, ?, ?, ?, ?)",
                (weapon_name, weapon_finish, weapon_quality, price, odds_range, odds))

# 提交交易
conn.commit()

# 列印出資料庫中的所有內容
c.execute("SELECT * FROM odds_history")
rows = c.fetchall()
for row in rows:
    print(row)

# 關閉連接
conn.close()

# 關閉瀏覽器
driver.quit()
