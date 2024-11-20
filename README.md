# 尚未完成

# 這個是一個有關於 「Skinclub」這個網站的小程式

## 目標：
- 找出Skinclub上的所有箱子
- 找出1到100k抽數的理論期望值
- 找出每個箱子最好的抽數和花費
- 依照有的金錢找出最好的箱子

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
- `main.py`：主程式文件
- `requirements.txt`：依賴包列表
- `README.md`：專案說明文件
- `test`：測試用資料夾，可以刪除

## 主要功能：
- 爬取 Skinclub 網站上的箱子資訊
- 計算每個箱子的期望值
- 儲存和列印結果到 SQLite 資料庫

## 注意事項：
- 請確保已安裝所有依賴包
- 請確保網路連接正常，以便爬取網站資料