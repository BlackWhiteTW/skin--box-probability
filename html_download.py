from requests_html import HTMLSession

# 建立 HTML 會話
session = HTMLSession()
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

# 發送 HTTP GET 請求並獲取網頁內容
response = session.get(url)
print(response.text)