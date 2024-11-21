# 找出箱子開出的物品和對應的價格、機率等資訊

from bs4 import BeautifulSoup

def box_open(html):
    # 如果 html 是字串，將其轉換為 BeautifulSoup 物件
    if isinstance(html, str):
        html = BeautifulSoup(html, 'html.parser')

    # 提取包含 class="row" 的所有元素
    rows = html.find_all('div', class_='row')
    print(len(rows))

    results = []

    # 進一步解析每個 row 中的內容
    for row in rows:
        item_cell = row.find('div', class_='cell item-cell')
        price_cell = row.find('div', class_='cell price-cell ellipsis')
        range_cell = row.find('div', class_='cell range-cell ellipsis')
        odds_cell = row.find('div', class_='cell odds-cell ellipsis')

        # 判斷是否找到了所有的 cell
        if item_cell and price_cell and range_cell and odds_cell:
            weapon_name = item_cell.find('span', class_='weapon-name').text.strip()
            weapon_finish = item_cell.find('span', class_='weapon-finish').text.strip()
            weapon_quality = item_cell.find('span', class_='quality').text.strip()
            price = price_cell.text.strip().replace('\n', '').replace(' ', '').replace('Price', '').replace('$', '')
            odds_range = range_cell.text.strip().replace('\n', '').replace(' ', '').replace('Range', '')
            odds = odds_cell.text.strip().replace('\n', '').replace(' ', '').replace('Odds', '').replace('%', '')

            # 將結果添加到列表中
            results.append({
                'weapon_name': weapon_name,
                'weapon_finish': weapon_finish,
                'weapon_quality': weapon_quality,
                'price': price,
                'odds_range': odds_range,
                'odds': odds
            })

    return results