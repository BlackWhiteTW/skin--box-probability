# 主要執行的程式

# 匯入套件
import os
from datetime import datetime, timedelta
import sys

# 確保當前目錄在 sys.path 中
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# 確保 ./main 目錄在 sys.path 中
main_dir = os.path.join(current_dir, 'main')
if main_dir not in sys.path:
    sys.path.append(main_dir)
    
# 匯入自己做的程式
from html_open import get_box_url
from html_download import get_box_code
from html_save import save_html
from map_and_rule import get_map_rule

# 檢查 skin_map.txt 的日期
def is_skin_map_outdated(file_path):
    if not os.path.exists(file_path):
        return True
    file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    return datetime.now() - file_mod_time > timedelta(days=30)

# 檢查 skin_map.txt 是否過期
skin_map_file = os.path.join(current_dir, 'skin_map.txt')
if is_skin_map_outdated(skin_map_file):
    print("skin_map.txt 已經超過一個月未更新，正在更新資料...")
    get_map_rule()
    print("skin_map.txt 已更新。")
else:
    print("skin_map.txt 是最新的。")

# 下載箱子的資料
box_name = get_box_url()

# 設定箱子的網址
skin_club_url = 'https://skin.club/cases/open/'

# 詢問是否要儲存HTML
save_html_bool = input("是否要下載並儲存個箱子的HTML? (Y/N): ").strip().lower() == 'y'

# 儲存資料 ( HTML ) ， 如果不需要儲存可以註解掉
if save_html_bool:
    language = ['en','zh-tw','zh-cn','ja','ko']
    save_languages = input("請輸入要儲存的語言 (en/zh-tw/zh-cn/ja/ko)，以逗號分隔: ").strip().lower().split(',')
    save_languages = [lang.strip() for lang in save_languages if lang.strip() in language]
    for lang in save_languages:
        for box in box_name:
            print(lang, box)
            print(f"{save_languages.index(lang) + 1} / {len(save_languages)} , {box_name.index(box) + 1} / {len(box_name)}")
            tmp = get_box_code(skin_club_url, box)
            save_html(tmp, box, lang)

