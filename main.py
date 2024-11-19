# 主要執行的程式

# 匯入套件
from requests_html import HTMLSession

# 匯入自己做的程式
from html_open import get_box_url
from html_download import get_box_code
from html_save import save_html

# 下載爬蟲規則和網頁地圖
session = HTMLSession()
url = "https://skin.club/robots.txt"
response = session.get(url)
skin_rule = "skin_rule.txt"
with open(skin_rule, 'w', encoding='utf-8') as f:
    f.write(response.text)
url = "https://skin.club/sitemap.xml"
response = session.get(url)
skin_map = "skin_map.txt"
with open(skin_map, 'w', encoding='utf-8') as f:
    f.write(response.text)

# 下載箱子的資料
box_name = get_box_url()
print(box_name)

skin_club_url = 'https://skin.club/cases/open/'

language = ['en','zh-tw','zh-cn','ja','ko']

for i in range(0,len(language)):
    for j in range(0,len(box_name)):
        print(language[i],box_name[j])
        print(f"{i+1} / {len(language)} , {j+1} / {len(box_name)}")
        tmp = get_box_code(skin_club_url, box_name[j])
        
        # 儲存資料 ( HTML ) ， 如果不需要儲存可以註解掉
        save_html(tmp, box_name[j],language[i])
        
        
