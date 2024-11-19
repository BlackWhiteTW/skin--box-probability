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
            if 'cases/open' in url_arr[j] and 'en' in url_arr[j]:
                box_find = url_arr[j].find('href="')
                box_rfind = url_arr[j].rfind('"')
                box_name = url_arr[j][box_find+6:box_rfind]
                box_url.append(box_name)
    box_url = list(set(box_url))
    box_names = set(url.split('/')[-1] for url in box_url)
    for name in box_names:
        print(f"Box: {name}")
    return list(box_names)

# 測試
get_box_url()
print(len(get_box_url()))
print("Done")
