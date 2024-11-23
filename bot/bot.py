import sys
import os
import json
import sqlite3
import matplotlib.pyplot as plt
import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

# 確保 ./main 目錄在 sys.path 中
current_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.join(current_dir, '..', 'main')
if main_dir not in sys.path:
    sys.path.append(main_dir)

# 匯入自己做的程式
from false_probability import get_box_data, calculate_theoretical_value
from html_open import get_box_url
from box_img import update_chart
from box_price import update_box_prices
from update import update_data

# 檢查 skin_map.txt 的日期
def is_skin_map_outdated(file_path):
    if not os.path.exists(file_path):
        return True
    file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    # 計算上次修改時間距離最近的周一的天數
    days_since_last_monday = (datetime.now() - file_mod_time).days % 7
    return days_since_last_monday > 0

# 讀取設定檔
set_json_path = os.path.join(current_dir, 'set.json')
with open(set_json_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

TOKEN = config['TOKEN']
activity = config['activity']
status = config['status']
thinking = config['thinking']
pronouns = config['pronouns']
introduction = config['introduction']

# 初始化 bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=activity), status=discord.Status.online)
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

@bot.tree.command(name='chart', description='查找箱子圖表')
async def chart(interaction: discord.Interaction, box_name: str):
    try:
        data = get_box_data(box_name)
        chart_path = generate_chart(data, box_name)
        await interaction.response.send_message(file=discord.File(chart_path))
    except sqlite3.OperationalError as e:
        await interaction.response.send_message(f'錯誤: {str(e)}')

@bot.tree.command(name='calculate', description='計算某箱子抽數和對應的回本率')
async def calculate(interaction: discord.Interaction, box_name: str, num_draws: int):
    try:
        data = get_box_data(box_name)
        total_value, average_value, total_cost, return_probability = calculate_theoretical_value(data, box_name, num_draws)
        await interaction.response.send_message(f'箱子: {box_name}\n抽數: {num_draws}\n總價值: {total_value}\n平均價值: {average_value}\n總成本: {total_cost}\n回本率: {return_probability}')
    except sqlite3.OperationalError as e:
        await interaction.response.send_message(f'錯誤: {str(e)}')

@bot.tree.command(name='best_box', description='計算幾美金對應最好的箱子')
async def best_box(interaction: discord.Interaction, budget: float):
    box_names = get_box_url()
    best_box_name = None
    best_return_probability = 0
    for box_name in box_names:
        data = get_box_data(box_name)
        box_price = get_box_price(box_name)
        if box_price == 0:
            continue
        num_draws = int(budget // box_price)
        if num_draws == 0:
            continue
        _, _, _, return_probability = calculate_theoretical_value(data, box_name, num_draws)
        if return_probability > best_return_probability:
            best_return_probability = return_probability
            best_box_name = box_name
    if best_box_name:
        await interaction.response.send_message(f'預算 ${budget} 最好的箱子是 {best_box_name}，回本率為 {best_return_probability}')
    else:
        await interaction.response.send_message(f'沒有找到適合預算 ${budget} 的箱子')

@bot.tree.command(name='check_update', description='檢查是否需要更新')
async def check_update(interaction: discord.Interaction):
    # 檢查 skin_map.txt 是否過期
    skin_map_file = os.path.join('data', 'skin_club', 'skin_map.txt')
    if is_skin_map_outdated(skin_map_file):
        print("skin_map.txt 已經超過一周未更新，正在更新資料...")
        update_data()
        print("skin_map.txt 已更新。")
        await interaction.response.send_message('skin_map.txt 已更新。')
    else:
        print("skin_map.txt 是最新的。")
        await interaction.response.send_message('skin_map.txt 是最新的。')

def generate_chart(data, box_name):
    chart_path = f'main/data_img/{box_name}_return_rate_chart.png'
    
    # 如果圖表已經存在，直接返回圖表路徑
    if os.path.exists(chart_path):
        return chart_path

    # 否則生成新的圖表
    draws = list(range(1, 100001, 100))
    if 100000 not in draws:
        draws.append(100000)
    total_values = []
    average_values = []
    total_costs = []
    return_probabilities = []
    for num_draw in draws:
        total_value, average_value, total_cost, return_probability = calculate_theoretical_value(data, box_name, num_draw)
        total_values.append(total_value)
        average_values.append(average_value)
        total_costs.append(total_cost)
        return_probabilities.append(return_probability)

    plt.figure(figsize=(10, 6))
    plt.plot(draws, return_probabilities, label='回報率')
    plt.xlabel('抽數')
    plt.ylabel('回報率')
    plt.title(f'{box_name} 抽數與回報率的關係')
    plt.legend()
    plt.grid(True)
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def get_box_price(box_name):
    conn = sqlite3.connect('main/data/_box_price.db')
    c = conn.cursor()
    c.execute("SELECT price FROM box_prices WHERE box_name = ?", (box_name,))
    box_price = c.fetchone()
    conn.close()
    return box_price[0] if box_price else 0.0

bot.run(TOKEN)