# 匯入套件
import os
from datetime import datetime

# 匯入自己做的程式
from update import update_data

# 檢查 skin_map.txt 的日期
def is_skin_map_outdated(file_path):
    if not os.path.exists(file_path):
        return True
    file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    # 計算上次修改時間距離最近的周一的天數
    days_since_last_monday = (datetime.now() - file_mod_time).days % 7
    return days_since_last_monday > 0

# 檢查 skin_map.txt 是否過期
def file_is_expired():
    skin_map_file = os.path.join('data', 'skin_club', 'skin_map.txt')
    if is_skin_map_outdated(skin_map_file):
        print("skin_map.txt 已經超過一周未更新，正在更新資料...")
        update_data()
        print("skin_map.txt 已更新。")
    else:
        print("skin_map.txt 是最新的。")

