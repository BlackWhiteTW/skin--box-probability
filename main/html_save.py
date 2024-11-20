# 定義要儲存的資料

import os
from bs4 import BeautifulSoup

def save_html(html, filename, language):
    save_path = f'../data/box_save_{language}/'
    os.makedirs(save_path, exist_ok=True)
    
    # 如果 html 是字串，將其轉換為 BeautifulSoup 物件
    if isinstance(html, str):
        html = BeautifulSoup(html, 'html.parser')
    
    with open(save_path + filename + '.html', 'w', encoding='utf-8') as f:
        f.write(html.prettify())