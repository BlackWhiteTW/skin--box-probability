import os
import sqlite3
from bs4 import BeautifulSoup
from html_open import get_box_url

def create_box_price_table():
    conn = sqlite3.connect('main/data/_box_price.db')
    c = conn.cursor()
    
    # 創建表格
    c.execute('''CREATE TABLE IF NOT EXISTS box_prices
                (box_name TEXT, price REAL)''')
    
    conn.commit()
    conn.close()

def extract_box_price(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    price_element = soup.find('p', class_='case-info__price')
    if price_element:
        price_text = price_element.text.strip().replace('$', '')
        try:
            price = float(price_text)
        except ValueError:
            price = 0.0
        return price
    return 0.0

def save_box_price(box_name, price):
    conn = sqlite3.connect('main/data/_box_price.db')
    c = conn.cursor()
    
    # 插入資料
    c.execute("INSERT INTO box_prices (box_name, price) VALUES (?, ?)", (box_name, price))
    
    conn.commit()
    conn.close()

def update_box_prices():
    # 創建表格
    create_box_price_table()
    
    # 取得所有箱子的名稱
    box_names = get_box_url()
    
    # 計算並儲存每個箱子的價格
    for box_name in box_names:
        file_path = f'data/box_save_zh-tw/{box_name}.html'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            price = extract_box_price(html_content)
            save_box_price(box_name, price)
            print(f"Saved price for {box_name}: {price}")
        else:
            print(f"File not found: {file_path}")

# 測試
if __name__ == "__main__":
    update_box_prices()