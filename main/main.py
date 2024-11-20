# 主要執行的程式

# 匯入套件
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import os

# 匯入自己做的程式
from html_open import get_box_url
from html_download import get_box_code
from html_save import save_html

# 下載爬蟲規則和網頁地圖
session = HTMLSession()
save_path = os.path.join('.', 'skin_club')
os.makedirs(save_path, exist_ok=True)

url = "https://skin.club/robots.txt"
response = session.get(url)
skin_rule = "skin_rule.txt"
with open(os.path.join(save_path, skin_rule), 'w', encoding='utf-8') as f:
    f.write(response.text)

url = "https://skin.club/sitemap.xml"
response = session.get(url)
skin_map = "skin_map.txt"
with open(os.path.join(save_path, skin_map), 'w', encoding='utf-8') as f:
    f.write(response.text)

# 下載箱子的資料
box_name = get_box_url()

# 設定箱子的網址
skin_club_url = 'https://skin.club/cases/open/'

language = ['en','zh-tw','zh-cn','ja','ko']

# 詢問是否要儲存HTML
save_html_bool = input("是否要下載並儲存個箱子的HTML? (Y/N): ").strip().lower() == 'y'

# 儲存資料 ( HTML ) ， 如果不需要儲存可以註解掉
if save_html_bool:
    save_languages = input("請輸入要儲存的語言 (en/zh-tw/zh-cn/ja/ko)，以逗號分隔: ").strip().lower().split(',')
    save_languages = [lang.strip() for lang in save_languages if lang.strip() in language]
    for lang in save_languages:
        for box in box_name:
            print(lang, box)
            print(f"{save_languages.index(lang) + 1} / {len(save_languages)} , {box_name.index(box) + 1} / {len(box_name)}")
            tmp = get_box_code(skin_club_url, box)
            save_html(tmp, box, lang)
