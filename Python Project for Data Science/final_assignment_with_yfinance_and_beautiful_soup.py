import yfinance as yf
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
beautiful_soup = BeautifulSoup(html_data, "html5lib")
table = beautiful_soup.find_all("tbody")[1]

game_stop_dict = []
for row in table.find_all("tr"):
    dict = {"Date": None, "Revenue": None}
    cols = row.find_all("td")
    i = 0
    for key in dict:
        dict[key] = cols[i].text
        i = i + 1
    game_stop_dict.append(dict)

gme_revenue = pd.DataFrame(game_stop_dict)
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace('[\\$,]',"", regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
print(gme_revenue.tail(5))

game_stop = yf.Ticker("GME")
gme_data = game_stop.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head())

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

make_graph(gme_data, gme_revenue, "GameStop")


# Question 5
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
# print(tesla_data.head())

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
beautiful_soup = BeautifulSoup(html_data, "html5lib")
table = beautiful_soup.find_all("tbody")[1]

tesla_dict = []
for row in table.find_all("tr"):
    dict = {"Date": None, "Revenue": None}
    cols = row.find_all("td")
    i = 0
    for key in dict:
        dict[key] = cols[i].text
        i = i + 1
    tesla_dict.append(dict)

tesla_revenue = pd.DataFrame(tesla_dict)
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace('[\\$,]',"", regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
# print(tesla_revenue.tail(5))

# Question 5
make_graph(tesla_data, tesla_revenue, "Tesla")


