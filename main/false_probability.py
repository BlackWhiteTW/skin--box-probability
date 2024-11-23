import sqlite3

# 解析箱子資料
def get_box_data(box_name):
    conn = sqlite3.connect(f'main/data/{box_name}.db')
    c = conn.cursor()
    c.execute("SELECT weapon_name, weapon_finish, weapon_quality, price, odds_range, odds FROM odds_history")
    data = c.fetchall()
    conn.close()
    return data

# 計算理論值、支付的錢和回本概率
def calculate_theoretical_value(data, box_name, num_draws):
    # 將資料轉換為適當的格式
    items = []
    for row in data:
        weapon_name, weapon_finish, weapon_quality, price, odds_range, odds = row
        price = float(price)
        odds_range = list(map(int, odds_range.split('-')))
        odds = float(odds)
        items.append({
            'weapon_name': weapon_name,
            'weapon_finish': weapon_finish,
            'weapon_quality': weapon_quality,
            'price': price,
            'odds_range': odds_range,
            'odds': odds
        })

    # 計算總獲得值
    total_value = 0
    for i in range(num_draws):
        position = i % 100000 + 1
        for item in items:
            if item['odds_range'][0] <= position <= item['odds_range'][1]:
                total_value += item['price']
                break

    # 平均獲得值
    average_value = total_value / num_draws

    # 計算支付的錢
    conn = sqlite3.connect('main/data/_box_price.db')
    c = conn.cursor()
    c.execute("SELECT price FROM box_prices WHERE box_name = ?", (box_name,))
    box_price = c.fetchone()
    conn.close()
    if box_price:
        box_price = box_price[0]
    else:
        box_price = 0.0
    total_cost = box_price * num_draws

    # 計算回本率
    if total_cost > 0:
        return_probability = total_value / total_cost
    else:
        return_probability = 0.0

    return total_value, average_value, total_cost, return_probability

if __name__ == '__main__':
    data = get_box_data('test_box')
    total_value, average_value, total_cost, return_probability = calculate_theoretical_value(data, 'test_box', 1000)
    print(f'Total Value: {total_value}')
    print(f'Average Value: {average_value}')
    print(f'Total Cost: {total_cost}')
    print(f'Return Probability: {return_probability}')