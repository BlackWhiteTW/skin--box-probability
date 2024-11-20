# 定義要儲存的資料

import os

def save_html(html, filename,language):
    save_path = f'./box_save_{language}/'
    os.makedirs(save_path, exist_ok=True)
    with open(save_path + filename + '.html', 'w', encoding='utf-8') as f:
        f.write(html.prettify())