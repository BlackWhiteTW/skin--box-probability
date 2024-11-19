from requests_html import HTMLSession
# import requests

def get_box_code(skin_club_url, box_name):
    
    session = HTMLSession()
    url = skin_club_url + box_name + "/odds-history"
    
    response = session.get(url)

    return response.text

# 廢棄的另一個方法 得到的結果和上面的方法一樣
"""
def download_box_code(skin_club_url, box_name):
    
    url = skin_club_url + box_name + "/odds-history"
    
    response = requests.get(url)
    
    response_int = response.text.find('div')
    response_text = response.text[response_int:]
    print(response_int)
    print(response_text)
    
    return response_text
"""

skin_club_url = 'https://skin.club/cases/open/'
box_name = 'ct_pistols_farm'
print(len(get_box_code(skin_club_url, box_name)))