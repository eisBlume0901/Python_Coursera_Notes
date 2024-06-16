import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

amd = yf.Ticker("AMD")

# Saving AMD's data into a json file
with open("amd.json", "w") as json_file:
    json.dump(amd.info, json_file)

# Opening AMD json and saving it ito amd_info variable
with open("amd.json") as json_file:
    amd_info = json.load(json_file)

# Question 1, Use key "country" to find the country the stock belongs to
print(amd_info["country"])

# Question 2, Use key "sector" to find the sector the stock belongs to
print(amd_info["sector"])

# Question 3, Obtain stock data for AMD using the history function, set the period
# to max. Find the "Volume" traded on the first day (first row)
pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

amd_share_price_data = amd.history(period="max")
amd_share_price_data.reset_index(inplace=True)
print(amd_share_price_data.iloc[0]["Volume"])


# apple = yf.Ticker("AAPL")
# print(apple.info)
#
# # Saving Apple's data into a json file
# with open("apple.json", "w") as json_file:
#     json.dump(apple.info, json_file)
#
# # Opening apple.json file and saving it to apple_info variable
# with open("apple.json") as json_file:
#     apple_info = json.load(json_file)
#
# print(apple_info["country"])
#
# # max - from the beginning where apple has stocks to present time
# apple_share_price_data = apple.history(period="max")
# print(apple_share_price_data.head())
#
# apple_share_price_data.reset_index(inplace=True)
# print(apple_share_price_data.head())
#
# apple_share_price_data.plot(x="Date", y="Open")
# plt.show()
#
# apple.dividends.plot()
# plt.show()