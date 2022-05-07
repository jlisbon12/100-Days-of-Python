import requests
from datetime import date
from datetime import timedelta
# from newsapi import NewsApiClient


STOCK = "AAPL"
COMPANY_NAME = "Apple Inc."

NEWS_KEY = "3493c8ecfd734f2897b86c0daa3b1373"
STOCK_KEY = "s88fECUCeS0JEZ62ub4tcRzA2_vRImD5"

yest = date.today() - timedelta(days=1)
day_before_yest = date.today() - timedelta(days=4)


news_param = {
    "q": "apple",
    "apiKey": NEWS_KEY,
    "from": f"{day_before_yest}",
    "to": f"{yest}",
    "sortBy": "popularity"
}


## STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://newsapi.org/v2/everything", params=news_param)
response.raise_for_status()
news_data = response.json()
news_articles = news_data['articles'][:3]
# for new in news_articles:
#     print(f"Headline: {new['title']}")
#     print(f"Brief: {new['description']}")

stock_param = {
    "apiKey": STOCK_KEY
}
r = requests.get(f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/{day_before_yest}/{yest}", params=stock_param)
r.raise_for_status()
stock_data = r.json()

day_before_close = stock_data['results'][0]['c']
yest_close = stock_data['results'][1]['c']
difference = abs(yest_close - day_before_close)
prcnt_diff = difference / yest_close
print(prcnt_diff)





## STEP 2: Use https://www.alphavantage.co
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

