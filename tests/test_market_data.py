import requests
import pytest

# Function to fetch data from the SZSE API
def fetch_market_data():
    url = "https://www.szse.cn/api/market/ssjjhq/getTimeData"
    params = {
        "random": "0.5928782276472836",
        "marketId": 1,
        "code": "000001",
        "language": "EN"
    }
    
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://www.szse.cn/English/siteMarketData/siteMarketDatas/lookup/index.html?code=000001"
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response

# Check the response status code = 200
def validate_market_data(response):
    if response.status_code != 200:
        raise Exception(f"Request failed with status code: {response.status_code}")
    
    data = response.json()
    high = data['data']['high']
    low = data['data']['low']
    
    if high > low:
        return high, low, True
    else:
        return high, low, False

# Verify that the "High" value is greater than the "Low" value
def test_market_data():
    response = fetch_market_data()
    high, low, verification_result = validate_market_data(response)
    
    print(f"High: {high}, Low: {low}, Verification Result: {verification_result}")
    
    assert verification_result, "High value is not greater than Low value."