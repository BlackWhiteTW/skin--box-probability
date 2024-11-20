from requests_html import HTMLSession
import os

# 下載爬蟲規則和網頁地圖
def get_map_rule():
    session = HTMLSession()
    save_path = os.path.abspath(os.path.join('.', 'data', 'skin_club'))
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

# 測試
print("test")
get_map_rule()
print("Done")