# 主要執行的程式

# 匯入套件
import os, sys, sqlite3
from selenium import webdriver
    
# 匯入自己做的程式
from html_open import get_box_url
from html_download import WebDriverManager
from html_save import save_html
from map_and_rule import get_map_rule
from box_open import box_open
from box_price import update_box_prices
from box_img import update_chart

def update_data():

    # 取得地圖和規則的資料
    get_map_rule()

    # 下載箱子的資料
    box_name = get_box_url()

    # 設定箱子的網址
    skin_club_url = 'https://skin.club/en/cases/'

    # 設定語言
    language = 'zh-tw'

    # 初始化 WebDriverManager
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    web_driver_manager = WebDriverManager(executable_path='/usr/bin/chromedriver')
    web_driver_manager.set_options(options)

    # 設定當前目錄
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 儲存資料 ( HTML ) 到 data/box_save_zh-tw
    # 警告：這個步驟會花費大量時間，且下載時會占用大量記憶體
    
    for box in box_name:
        print(language, box)
        print(f"{box_name.index(box) + 1} / {len(box_name)}")
        tmp = web_driver_manager.get_box_code(skin_club_url, box)
        save_html(tmp, box, language)
    
    print("Downloaded all box data")
    
    # 將以下載的箱子資料做處理並儲存到main/data
    processed_boxes = []
    box_arr = []

    # 處理箱子資料
    for box in box_name:
        if box in processed_boxes:
            continue

        file_path = os.path.join(current_dir, 'data', 'box_save_' + language, box + '.html')
        print(file_path)
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            file_open = f.read()
        result = box_open(file_open)
        if result or result != []:
            processed_boxes.append(box)
            box_arr.append(result)

        else:
            print(f"Failed to parse: {file_path}")

    print("-"*50)
    print(processed_boxes)
    print(len(processed_boxes))
    print("-"*50)
    print(box_arr)
    print(len(box_arr))
    
    print("Processed all box data")
    
    # 儲存處理後的箱子資料到 main/data
    output_dir = os.path.join(current_dir, 'main', 'data')
    os.makedirs(output_dir, exist_ok=True)
    print("Saving processed box data")
    # 儲存箱子資料到 SQLite 資料庫
    for box, data in zip(processed_boxes, box_arr):
        
        print(f"Saving {box}.db")
        
        
        # 連接到 SQLite 資料庫
        conn = sqlite3.connect(f'main/data/{box}.db')
        c = conn.cursor()

        # 檢查表格是否存在
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='odds_history'")
        if c.fetchone() is not None:
            # 清空表格資料
            c.execute('DELETE FROM odds_history')
        # 建立表格
        c.execute(
        '''CREATE TABLE IF NOT EXISTS odds_history
                    (weapon_name TEXT, weapon_finish TEXT, weapon_quality TEXT, price TEXT, odds_range TEXT, odds TEXT)''')

        for item in data:
            weapon_name = item.get('weapon_name', '')
            weapon_finish = item.get('weapon_finish', '')
            weapon_quality = item.get('weapon_quality', '')
            price = item.get('price', '')
            odds_range = item.get('odds_range', '')
            odds = item.get('odds', '')

            c.execute("INSERT INTO odds_history (weapon_name, weapon_finish, weapon_quality, price, odds_range, odds) VALUES (?, ?, ?, ?, ?, ?)",
                    (weapon_name, weapon_finish, weapon_quality, price, odds_range, odds))

        # 提交交易
        conn.commit()
    print("Saved all processed box data")
    # 更新箱子價格  
    update_box_prices()
    print("Updated all box prices")
    # 關閉 WebDriver
    web_driver_manager.quit()
    print("Closed WebDriver")
    
    # 更新 img 檔案
    for box in box_name:
        update_chart(box)
    print("Updated all img files")

if __name__ == '__main__':
    update_data()