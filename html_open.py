from requests_html import HTMLSession

def get_box_url():
    # 建立 HTML 會話
    session = HTMLSession()
    url = 'https://skin.club/sitemap.xml'
    box_url = []
    response = session.get(url)
    response_arr = response.text.split('<url>')
    for i in range(1, len(response_arr)):
        url_arr = response_arr[i].split('<xhtml:link')
        for j in range(1, len(url_arr)):
            if 'zh-TW' in url_arr[j] and 'cases/open' in url_arr[j]:
                box_find = url_arr[j].find('href="')
                box_rfind = url_arr[j].rfind('"')
                box_name = url_arr[j][box_find+6:box_rfind]
                box_url.append(box_name)
    box_url = list(set(box_url))
    for i in range(len(box_url)):
        print(box_url[i])
    return box_url

box_url = get_box_url()
print(len(box_url))