import requests
import smtplib
import datetime
from datetime import timedelta
BOT_KEY = MY_TOKEN
BOT_NAME = 'stock_bot'
BOT_USERNAME = "stock_pusher_bot"
BOT_ENDPOINT = f"https://api.telegram.org/bot{BOT_KEY}/sendMessage"
CHAT_ID = MY_CHAT
STOCK = "TSLA"
my_email = "arthur.conan.varvar@gmail.com"
password = MY_PASS
COMPANY_NAME = "Tesla Inc"
API_KEY = "XLI50CNDZA89DNZN"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "04b0f3d7e26849e1b174a60766ab076f"


def send_telegram():
    parameters_bot = {
        "chat_id": CHAT_ID,
        "text": f"TThe rate has changed: today: {delta}%, yesterday: {delta1}%\n" 
               f"Reason: - {news_list[0]},\n {news_list[1]} \n{news_list[2]} \n {news_list[3]} \n {news_list[4]} \n"
    }
    response = requests.post(BOT_ENDPOINT, params=parameters_bot)
    response.raise_for_status()


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        text = f"The rate has changed: today: {delta}%, yesterday: {delta1}%\n" \
               f"Reason: - {news_list[0]},\n {news_list[1]}, \n{news_list[2]}, \n {news_list[3]}, \n {news_list[4]}, \n"
        connect.sendmail(from_addr=my_email, to_addrs="iurii.ponomar@gmail.com",
                         msg=f"Subject: BITCOIN NEWS \n\n{text}")
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
today = datetime.datetime.utcnow()
today_date = today.date()
yesterday_date = today_date - timedelta(1)


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=XLI50CNDZA89DNZN'
r = requests.get(url)
r.raise_for_status()
data = r.json()
sliced_data_today = data["Time Series (Digital Currency Daily)"][str(today_date)]
sliced_data_yesterday = data["Time Series (Digital Currency Daily)"][str(yesterday_date)]
sliced_data_day_before = data["Time Series (Digital Currency Daily)"][str(yesterday_date - timedelta(1))]
delta = float(sliced_data_today["4a. close (USD)"]) - float(sliced_data_yesterday["4a. close (USD)"])
delta1 = float(sliced_data_yesterday["4a. close (USD)"]) - float(sliced_data_day_before["4a. close (USD)"])

delta = round((delta / float(sliced_data_today["4a. close (USD)"])) * 100)
delta1 = round((delta1 / float(sliced_data_yesterday["4a. close (USD)"])) * 100)


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
## STEP 2: Use https://newsapi.org/docs/endpoints/everything

URL_NEWS = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=04b0f3d7e26849e1b174a60766ab076f'
r = requests.get(URL_NEWS)
r.raise_for_status()
data = r.json()
news_list = [data["articles"][i]['title'] for i in range(5)]

# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
send_email()
send_telegram()

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

