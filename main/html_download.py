# 下載網頁的html檔案

from requests_html import HTMLSession

def get_box_code(skin_club_url, box_name):
    session = HTMLSession()
    url = skin_club_url + box_name + "/odds-history"
    
    response = session.get(url)

    return response.text

# 測試
print("test")
skin_club_url = 'https://skin.club/cases/open/'
box_name = 'ct_pistols_farm'
print(len(get_box_code(skin_club_url, box_name)))
print("Done")