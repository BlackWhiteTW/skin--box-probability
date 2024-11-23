<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** Markdown "badges" can be added here to provide quick links to various resources.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See https://shields.io for more badge options.
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BlackWhiteTW/skin--box-probability">
    <img src="images/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Skinclub 小程式</h3>

  <p align="center">
    用於分析和計算 Skinclub 網站上箱子的期望值。
    <br />
    <a href="https://github.com/BlackWhiteTW/skin--box-probability"><strong>探索文件 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BlackWhiteTW/skin--box-probability/issues">報告 Bug</a>
    ·
    <a href="https://github.com/BlackWhiteTW/skin--box-probability/issues">提出新功能</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>目錄</summary>
  <ol>
    <li>
      <a href="#關於專案">關於專案</a>
      <ul>
        <li><a href="#建置原因">建置原因</a></li>
        <li><a href="#使用技術">使用技術</a></li>
      </ul>
    </li>
    <li>
      <a href="#快速開始">快速開始</a>
      <ul>
        <li><a href="#下載與安裝">下載與安裝</a></li>
        <li><a href="#配置">配置</a></li>
        <li><a href="#運行">運行</a></li>
      </ul>
    </li>
    <li><a href="#文件結構">文件結構</a></li>
    <li><a href="#主要功能">主要功能</a></li>
    <li><a href="#注意事項">注意事項</a></li>
    <li><a href="#貢獻">貢獻</a></li>
    <li><a href="#聯絡方式">聯絡方式</a></li>
    <li><a href="#致謝">致謝</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## 關於專案

這是一個有關於「Skinclub」這個網站的小程式，用於分析和計算箱子的期望值。

### 建置原因

- 找出 Skinclub 上的所有箱子
- 統計每個箱子的概率和內容
- 找出 1 到 100k 抽數的理論期望值(圖表：可以看出大致曲線)
- 依照有的金錢找出最好的箱子

### 使用技術

此專案使用以下技術：

- [Python](https://www.python.org/)
- [Discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests-HTML](https://requests-html.kennethreitz.org/)

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>

<!-- GETTING STARTED -->
## 快速開始

### 下載與安裝

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

### 配置

4. 創建並配置 `set.json` 文件。
    ```json
    {
        "TOKEN": "your_discord_bot_token",
        "activity": "Skinclub",
        "status": "online",
        "thinking": "Calculating probabilities",
        "pronouns": "they/them",
        "introduction": "我是你就賭了！！！"
    }
    ```

### 運行

5. 運行主程式。
    ```bash
    python bot.py
    ```

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>

<!-- FILE STRUCTURE -->
## 文件結構

- `bot/`
  - `bot.py`：Discord 機器人主程式。
  - `set.json`：配置文件，包含 Discord 機器人的設定，例如 TOKEN、活動狀態、自我介紹等。
- `data/`
  - `box_save_zh-tw/`：儲存下載的 HTML 檔案。
  - `skin_club/`：儲存爬蟲規則和網頁地圖。
- `main/`
  - `box_img.py`：生成箱子回報率圖表。
  - `box_open.py`：解析箱子開出的物品和對應的價格、機率等資訊。
  - `box_price.py`：計算並儲存每個箱子的價格。
  - `data/`：儲存處理後的箱子資料。
  - `data_img/`：儲存生成的圖表。
  - `false_probability.py`：計算理論值、支付的錢和回本概率。
  - `html_download.py`：下載網頁的 HTML 檔案。
  - `html_open.py`：打開網頁地圖，找出所有箱子的網址。
  - `html_save.py`：儲存 HTML 內容。
  - `map_and_rule.py`：下載爬蟲規則和網頁地圖。
  - `update.py`：主要執行的程式，負責整個程式的執行流程。
- `test/`
  - `test.html`：測試用 HTML 檔案。
  - `test.py`：測試程式。
- `README.md`：專案說明文件，提供專案的簡介、使用方法和文件結構。
- `requirements.txt`：依賴包列表，包含程式運行所需的所有 Python 庫。

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>

<!-- FEATURES -->
## 主要功能

- 爬取 Skinclub 網站上的箱子資訊：
  - 使用 `html_open.py` 來打開網頁地圖，找出所有箱子的網址。
  - 使用 `html_download.py` 來下載網頁的 HTML 檔案。
  - 使用 `html_save.py` 來儲存 HTML 內容。
  - 使用 `box_open.py` 來解析箱子開出的物品和對應的價格、機率等資訊。
- 計算每個箱子的期望值：
  - 解析下載的 HTML 內容，提取箱子開出的物品和對應的價格、機率等。
- 儲存和列印結果到 SQLite 資料庫：
  - 將解析和計算的結果儲存到 SQLite 資料庫中，方便後續查詢和分析。

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>

<!-- USAGE -->
## 注意事項

- 請確保已安裝所有依賴包：
  - 可以使用 `pip install -r requirements.txt` 來安裝所有依賴包。
- 請確保網路連接正常，以便爬取網站資料：
  - 程式需要訪問 Skinclub 網站來爬取箱子資訊，請確保網路連接正常。

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>

<!-- CONTRIBUTING -->
## 貢獻

我還不會用這個東西，之後再來研究

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>

<!-- CONTACT -->
## 聯絡方式

你的名字 - [@blackwhite_0322](https://twitter.com/blackwhite_0322) - 9131419hihi@gmail.com

專案連結: [https://github.com/BlackWhiteTW/skin--box-probability](https://github.com/BlackWhiteTW/skin--box-probability)

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## 致謝

感謝以下資源和工具：

- [othneildrew's Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [Python](https://www.python.org/)
- [Discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests-HTML](https://requests-html.kennethreitz.org/)

<p align="right">(<a href="#readme-top">回到頂部</a>)</p>