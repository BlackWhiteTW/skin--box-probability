import sqlite3
import os
import matplotlib.pyplot as plt

from html_open import get_box_url
from false_probability import calculate_theoretical_value

box_name = get_box_url()

def get_box_data(box_name):
    db_path = f'main/data/{box_name}.db'
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file {db_path} does not exist.")
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT weapon_name, weapon_finish, weapon_quality, price, odds_range, odds FROM odds_history")
    data = c.fetchall()
    conn.close()
    return data

def generate_chart(data, box_name):
    draws = list(range(1, 100001, 2500))
    if 100000 not in draws:
        draws.append(100000)
    total_values = []
    average_values = []
    total_costs = []
    return_probabilities = []
    for num_draw in draws:
        print(f'Calculating for {num_draw} draws...')
        total_value, average_value, total_cost, return_probability = calculate_theoretical_value(data, box_name, num_draw)
        total_values.append(total_value)
        average_values.append(average_value)
        total_costs.append(total_cost)
        return_probabilities.append(return_probability)

    plt.figure(figsize=(10, 6))
    plt.plot(draws, return_probabilities, label='Return Rate')
    plt.xlabel('Number of Draws')
    plt.xticks(range(0, 100001, 10000))
    plt.ylabel('Return Rate')
    plt.yticks([i/10 for i in range(0, 11)])
    plt.title(f'{box_name} Return Rate vs Number of Draws')
    plt.legend()
    plt.grid(True)
    chart_path = f'main/data_img/{box_name}_return_rate_chart.png'
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def update_chart(box_name):
    data = get_box_data(box_name)
    
    print(f'Generating chart for {box_name}...')
    chart_path = generate_chart(data, box_name)
    print(f'Chart saved at {chart_path}')

if __name__ == '__main__':
    update_chart(box_name)
    print(f'{box_name} chart updated.')