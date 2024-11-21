# Skinclub 小程式

這是一個有關於「Skinclub」這個網站的小程式，用於分析和計算箱子的期望值。

## 目標：
- 找出 Skinclub 上的所有箱子
- 統計每個箱子的概率和內容
- 計算每多一抽的期望值 `尚未完成`
- 找出 1 到 100k 抽數的理論期望值 `尚未完成`
- 找出每個箱子最好的抽數和花費 `尚未完成`
- 依照有的金錢找出最好的箱子 `尚未完成`

## 使用方法：
1. 下載此存儲庫到本地。
    ```bash
    git clone https://github.com/BlackWhiteTW/skin--box-probability.git
    ```
2. 進入專案目錄。
    ```bash
    cd skin--box-probability
    ```
3. 安裝所需的依賴。
    ```bash
    pip install -r requirements.txt
    ```
4. 運行主程式。
    ```bash
    python main.py
    ```

## 文件結構：
- `main.py`：主程式文件，負責整個程式的執行流程。
- `requirements.txt`：依賴包列表，包含程式運行所需的所有 Python 庫。
- `README.md`：專案說明文件，提供專案的簡介、使用方法和文件結構。
- `test`：測試用資料夾，可以刪除。
- `html_open.py`：用於打開網頁地圖，找出所有箱子的網址。
- `html_download.py`：用於下載網頁的 HTML 檔案。
- `html_save.py`：用於儲存 HTML 內容。
- `map_and_rule.py`：用於下載爬蟲規則和網頁地圖。
- `box_open.py`：用於解析箱子開出的物品和對應的價格、機率等資訊。

## 主要功能：
- 爬取 Skinclub 網站上的箱子資訊：
  - 使用 `html_open.py` 來打開網頁地圖，找出所有箱子的網址。
  - 使用 `html_download.py` 來下載網頁的 HTML 檔案。
  - 使用 `html_save.py` 來儲存 HTML 內容。
  - 使用 `box_open.py` 來解析箱子開出的物品和對應的價格、機率等資訊。
- 計算每個箱子的期望值：
  - 解析下載的 HTML 內容，提取箱子開出的物品和對應的價格、機率等資訊。
  - 計算每個箱子的期望值，找出最好的抽數和花費。 `尚未完成`
- 儲存和列印結果到 SQLite 資料庫：
  - 將解析和計算的結果儲存到 SQLite 資料庫中，方便後續查詢和分析。 `尚未完成`

## 注意事項：
- 請確保已安裝所有依賴包：
  - 可以使用 `pip install -r requirements.txt` 來安裝所有依賴包。
- 請確保網路連接正常，以便爬取網站資料：
  - 程式需要訪問 Skinclub 網站來爬取箱子資訊，請確保網路連接正常。