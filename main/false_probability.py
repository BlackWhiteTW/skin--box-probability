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
def calculate_theoretical_value(box_name, num_draws):
    data = get_box_data(box_name)

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
    step = 100000 // (num_draws + 1)
    for i in range(1, num_draws + 1):
        position = i * step
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

# 回傳結果
def get_theoretical_value(box_name, num_draws):
    total_value, average_value, total_cost, return_probability = calculate_theoretical_value(box_name, num_draws)
    return total_value, average_value, total_cost, return_probability

# 測試
if __name__ == "__main__":
    box_name = "25-anniversary"
    num_draws = 4
    total_value, average_value, total_cost, return_probability = get_theoretical_value(box_name, num_draws)
    print(f"{box_name} 已抽取 {num_draws} 抽")
    print(f"總獲得: {total_value}")
    print(f"平均獲得: {average_value}")
    print(f"總花費: {total_cost}")
    print(f"回本率: {return_probability}")