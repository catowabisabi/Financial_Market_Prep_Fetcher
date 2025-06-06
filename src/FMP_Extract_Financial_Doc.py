#!/usr/bin/env python3
"""
# 這是一個用來抓取財務資訊的腳本，資料來源為 Financial Modeling Prep (FMP)。
# This script scrapes financial information from the Financial Modeling Prep (FMP) website.

# 官方網站：https://financialmodelingprep.com/developer/
# Official site: https://financialmodelingprep.com/developer/

# 使用免費方案（Free Plan）說明：
#   優點（Upside）:
#     - 更容易使用，相較 Yahoo 等競爭對手更開放
#     - 提供透明的計算公式與財務比率說明（多數其他網站沒有這種透明度）
#   缺點（Downside）:
#     - 每天最多僅 250 次 API 請求
#     - 若需更多請求數，可考慮升級帳戶（Upgrade with a plan）

# 提供的財務數據包括（Data Included）:
#   - Income Statements（損益表）
#   - Balance Sheets（資產負債表）
#   - Cash Flow Statements（現金流量表）
#   - Statistics（統計數據）

# API 請求參數說明（Parameter Specification）:
#   - ticker : 股票代碼，例如 "AAPL"（Company stock symbol）
#   - limit  : 每筆資料的最大筆數（Number of records to return per entry）
#   - key    : 註冊帳號後取得的 API 金鑰（API key assigned to your account）
#   - period : 報表類型，可選 "annual" 或 "quarter"（Reporting period: annual or quarter）

# 使用建議：
#   - 建議記錄已使用的 API 次數，避免超出每日限制
#   - 若分析多支股票，請加上時間延遲（如 time.sleep）以避免觸發限制

"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import FMP_Financial_Data_Scraping as fds
import pandas as pd
if __name__ == "__main__":
    """Running the scraper to obtain financial data."""
    key = pd.read_csv('config/Key.txt', header=None)[0][0]
    tickers = pd.read_csv('config/tickers.txt', header=None)[0] 
    
    for t in tickers:
        IS = fds.get_income_statement(ticker=t, limit=6, key=key, period='annual')
        BS = fds.get_balance_sheet(ticker=t, limit=6, key=key, period='annual')
        CF = fds.get_cash_flow_statement(ticker=t, limit=6, key=key, period='annual')
        FR = fds.get_financial_ratios(ticker=t, limit=6, key=key, period='annual')
        KM = fds.get_key_metrics(ticker=t, limit=6, key=key, period='annual')
        P = fds.get_daily_prices(ticker=t, timeseries=5*261, key=key)
        EV = fds.get_enterprise_value(ticker=t, rate=5*261, key=key, period='annual')
        # Creating a writer
        writer = pd.ExcelWriter('../data/{}.xlsx'.format(t), engine='xlsxwriter')
        # Putting into excel file.
        IS.to_excel(writer, sheet_name='Income Statement')
        BS.to_excel(writer, sheet_name='Balance Sheet Statement')
        CF.to_excel(writer, sheet_name='Cash Flow Statement')
        FR.to_excel(writer, sheet_name='Financial Ratios')
        KM.to_excel(writer, sheet_name='Key Metrics')
        P.to_excel(writer, sheet_name='Daily Prices')
        EV.to_excel(writer, sheet_name='Enterprise Value')
        # Saving the writer.
        writer.save()
        print('Finished with :', t) 