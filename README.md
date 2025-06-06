# Financial Market Prep Fetcher

This project fetches financial data from the [Financial Modeling Prep API](https://financialmodelingprep.com/developer/).

---

# 金融市場數據抓取工具

本專案旨在使用 [Financial Modeling Prep API](https://financialmodelingprep.com/developer/) 來抓取金融市場的相關數據。

## 繁體中文

### 功能
- 抓取公司的損益表、資產負債表、現金流量表。
- 獲取財務比率、關鍵指標和企業價值。
- 獲取每日股價。
- 將所有數據保存到一個 Excel 檔案中，並以不同的工作表分頁。

### 安裝與設定
1.  複製此專案到您的本地端：
    ```bash
    git clone <repository-url>
    cd Financial_Market_Prep_Fetcher
    ```
2.  安裝所需的 Python 套件：
    ```bash
    pip install -r requirements.txt
    ```
3.  設定您的 API 金鑰：
    -   打開 `config/Key.txt` 文件。
    -   將 `YOUR_API_KEY_HERE` 替換為您從 Financial Modeling Prep 網站上獲得的真實 API 金鑰。

4.  編輯您想抓取股票的公司代碼：
    -   打開 `config/tickers.txt` 文件。
    -   每行輸入一個公司代碼 (例如 AAPL, GOOG, TSLA)。

### 如何執行
-   在終端機中，執行以下指令：
    ```bash
    python src/FMP_Extract_Financial_Doc.py
    ```
-   腳本會為 `tickers.txt` 中的每個公司代碼建立一個對應的 `.xlsx` 檔案，並將其儲存在 `data/` 文件夾中。

### 文件夾結構
```
Financial_Market_Prep_Fetcher/
├── config/
│   ├── Key.txt           # 您的 API 金鑰
│   └── tickers.txt       # 要抓取的公司代碼列表
├── data/                 # 儲存輸出的 Excel 檔案
├── src/
│   ├── FMP_Extract_Financial_Doc.py      # 主要執行腳本
│   └── FMP_Financial_Data_Scraping.py  # API 呼叫的模組
├── README.md             # 專案說明文件
├── analysis.ipynb        # 數據分析的 Jupyter Notebook
└── requirements.txt      # Python 相依套件列表
```

### 數據分析
專案內包含一個 `analysis.ipynb` Jupyter Notebook，提供對抓取數據的初步分析與視覺化。

1.  確保您已完成數據抓取 (`python src/FMP_Extract_Financial_Doc.py`)。
2.  在專案根目錄下，啟動 Jupyter Lab：
    ```bash
    jupyter lab
    ```
3.  在打開的瀏覽器頁面中，點擊並打開 `analysis.ipynb`。
4.  您可以執行筆記本中的程式碼區塊，來查看分析結果。

---

## English

### Features
- Fetches company Income Statements, Balance Sheets, and Cash Flow Statements.
- Retrieves Financial Ratios, Key Metrics, and Enterprise Values.
- Gets daily stock prices.
- Saves all data into a single Excel file, with each data type in a separate sheet.

### Setup and Configuration
1.  Clone the repository to your local machine:
    ```bash
    git clone <repository-url>
    cd Financial_Market_Prep_Fetcher
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure your API Key:
    -   Open the `config/Key.txt` file.
    -   Replace `YOUR_API_KEY_HERE` with your actual API key from the Financial Modeling Prep website.

4.  Edit the list of stock tickers you want to fetch:
    -   Open the `config/tickers.txt` file.
    -   Enter one ticker per line (e.g., AAPL, GOOG, TSLA).

### How to Run
-   In your terminal, execute the following command:
    ```bash
    python src/FMP_Extract_Financial_Doc.py
    ```
-   The script will create an `.xlsx` file for each ticker in `tickers.txt` and save it in the `data/` directory.

### Folder Structure
```
Financial_Market_Prep_Fetcher/
├── config/
│   ├── Key.txt           # Your API Key
│   └── tickers.txt       # List of tickers to fetch
├── data/                 # Stores the output Excel files
├── src/
│   ├── FMP_Extract_Financial_Doc.py      # Main execution script
│   └── FMP_Financial_Data_Scraping.py  # Module for API calls
├── README.md             # This README file
├── analysis.ipynb        # Jupyter Notebook for data analysis
└── requirements.txt      # List of Python dependencies
```

### Data Analysis
The project includes an `analysis.ipynb` Jupyter Notebook for preliminary analysis and visualization of the fetched data.

1.  Ensure you have already fetched the data by running `python src/FMP_Extract_Financial_Doc.py`.
2.  In the project root directory, start Jupyter Lab:
    ```bash
    jupyter lab
    ```
3.  In the browser tab that opens, click on `analysis.ipynb` to open it.
4.  You can run the cells in the notebook to see the analysis. 