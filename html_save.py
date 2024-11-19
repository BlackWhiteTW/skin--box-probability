# 定義要儲存的資料
def save_html(html, filename,language):
    save_path = f'./box_save_{language}/'
    import os
    os.makedirs(save_path, exist_ok=True)
    with open(save_path + filename, 'w', encoding='utf-8') as f:
        f.write(html)