#!/usr/bin/env python3
"""This houses all the important functions that are called in the script."""
import pandas as pd
import requests

# 提取incme statement
def get_income_statement(ticker, limit, key, period='annual'):
    """Obtain income statement from the website"""
    URL = ('https://financialmodelingprep.com/api/v3/income-statement/{}?period={}&limit={}&apikey={}')
    r = requests.get(URL.format(ticker, period, limit, key))
    if r.status_code != 200 or not r.json():
        print(f"Error for {ticker} (Income Statement): {r.json().get('Error Message', r.text)}")
        return pd.DataFrame()
    incomeStatement = pd.DataFrame.from_dict(r.json()).transpose()
    # Cleaning the data
    incomeStatement.columns = incomeStatement.iloc[1]
    return incomeStatement[2:]

def get_balance_sheet(ticker, limit, key, period='annual'):
    """Obtain balance sheet statement from the website"""
    URL = ('https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}?period={}&limit={}&apikey={}')
    r = requests.get(URL.format(ticker, period, limit, key))
    if r.status_code != 200 or not r.json():
        print(f"Error for {ticker} (Balance Sheet): {r.json().get('Error Message', r.text)}")
        return pd.DataFrame()
    balanceSheet = pd.DataFrame.from_dict(r.json()).transpose()
    # Cleaning the data
    balanceSheet.columns = balanceSheet.iloc[1]
    return balanceSheet[2:]

def get_cash_flow_statement(ticker, limit, key, period='annual'):
    """Obtain cash flow statement from the website"""
    URL = ('https://financialmodelingprep.com/api/v3/cash-flow-statement/{}?period={}&limit={}&apikey={}')
    r = requests.get(URL.format(ticker, period, limit, key))
    if r.status_code != 200 or not r.json():
        print(f"Error for {ticker} (Cash Flow): {r.json().get('Error Message', r.text)}")
        return pd.DataFrame()
    cashFlow = pd.DataFrame.from_dict(r.json()).transpose()
    # Cleaning the data
    cashFlow.columns = cashFlow.iloc[1]
    return cashFlow[2:]

def get_financial_ratios(ticker, limit, key, period='annual'):
    """Obtain financial ratios from the website"""
    URL = ('https://financialmodelingprep.com/api/v3/ratios/{}?period={}&limit={}&apikey={}')
    r = requests.get(URL.format(ticker, period, limit, key))
    if r.status_code != 200 or not r.json():
        print(f"Error for {ticker} (Financial Ratios): {r.json().get('Error Message', r.text)}")
        return pd.DataFrame()
    financialRatios = pd.DataFrame.from_dict(r.json()).transpose()
    # Cleaning the data
    financialRatios.columns = financialRatios.iloc[1]
    return financialRatios[2:]

def get_key_metrics(ticker, limit, key, period='annual'):
    """Obtain key metrics from the website"""
    URL = ('https://financialmodelingprep.com/api/v3/key-metrics/{}?period={}&limit={}&apikey={}')
    r = requests.get(URL.format(ticker, period, limit, key))
    if r.status_code != 200 or not r.json():
        print(f"Error for {ticker} (Key Metrics): {r.json().get('Error Message', r.text)}")
        return pd.DataFrame()
    keyMetrics = pd.DataFrame.from_dict(r.json()).transpose()
    # Cleaning the data
    keyMetrics.columns = keyMetrics.iloc[1]
    return keyMetrics[2:]

def get_daily_prices(ticker, timeseries, key):
    """Obtain daily prices from the website"""
    URL = ('https://financialmodelingprep.com/api/v3/historical-price-full/{}?timeseries={}&apikey={}')
    r = requests.get(URL.format(ticker, timeseries, key))
    if r.status_code != 200 or not r.json() or 'historical' not in r.json():
        print(f"Error for {ticker} (Daily Prices): {r.json().get('Error Message', r.text)}")
        return pd.DataFrame()
    prices = pd.DataFrame.from_dict(r.json()['historical'])
    # Re-ordering the data
    prices = prices.reindex(index=prices.index[::-1])
    return prices

def get_enterprise_value(ticker, rate, key, period='annual'):
    """Obtain enterprise value from the website"""
    URL = ('https://financialmodelingprep.com/api/v3/enterprise-values/{}?period={}&limit={}&apikey={}')
    r = requests.get(URL.format(ticker, period, rate, key))
    if r.status_code != 200 or not r.json():
        print(f"Error for {ticker} (Enterprise Value): {r.json().get('Error Message', r.text)}")
        return pd.DataFrame()
    enterpriseValue = pd.DataFrame.from_dict(r.json()).transpose()
    # Cleaning the data
    enterpriseValue.columns = enterpriseValue.iloc[1]
    return enterpriseValue[2:]