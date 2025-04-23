import pandas as pd
import numpy as np
from datetime import datetime

def yen_investment_analysis(input_data):
    input_data["Real Rate KR"] = input_data["KR Interest Rate (%)"] - input_data["KR CPI (%)"]
    input_data["Real Rate JP"] = input_data["JP Interest Rate (%)"] - input_data["JP CPI (%)"]
    input_data["Real Rate Diff (KR - JP)"] = input_data["Real Rate KR"] - input_data["Real Rate JP"]

    expected_return = 2.5
    input_data["Sharpe Ratio (가정)"] = (expected_return - 3.5) / input_data["FX Volatility (%)"]

    def score(value, thresholds):
        if value <= thresholds[0]: return 1
        elif value <= thresholds[1]: return 2
        elif value <= thresholds[2]: return 3
        elif value <= thresholds[3]: return 4
        else: return 5

    input_data["Risk Score (CDS)"] = score(input_data["CDS Korea (bp)"], [20, 40, 60, 80])
    input_data["Hedge Cost Score"] = score(input_data["Hedging Cost (%)"], [0.5, 1.0, 1.5, 2.0])
    input_data["Volatility Score"] = score(input_data["FX Volatility (%)"], [0.5, 1.0, 1.5, 2.0])
    input_data["Sharpe Score"] = score(input_data["Sharpe Ratio (가정)"], [-1, 0, 1, 2])

    input_data["Investment Score (총점)"] = (
        6 - input_data["Risk Score (CDS)"] +
        6 - input_data["Hedge Cost Score"] +
        6 - input_data["Volatility Score"] +
        input_data["Sharpe Score"]
    )

    return input_data

def sample_input():
    return pd.DataFrame([{
        "Date": datetime.today().strftime('%Y-%m-%d'),
        "JPY/KRW": 1005.86,
        "KR Interest Rate (%)": 3.5,
        "JP Interest Rate (%)": 0.1,
        "US Interest Rate (%)": 5.25,
        "KR CPI (%)": 2.8,
        "JP CPI (%)": 2.0,
        "USD/KRW": 1350.25,
        "JP Trade Balance (¥B)": 180,
        "KR Trade Balance ($B)": 3.2,
        "FX Reserve (KR, $B)": 420,
        "CDS Korea (bp)": 38,
        "Hedging Cost (%)": 1.8,
        "FX Volatility (%)": 1.05
    }])
