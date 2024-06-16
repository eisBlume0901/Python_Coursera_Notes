import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")
table = soup.find("table")

amazon_dict = []
for row in table.find("tbody").find_all("tr"):
    dict = {"Date": None, "Open": None, "High": None, "Low": None,
            "Close": None, "Adj_Close": None,   "Volume": None}
    cols = row.find_all("td")
    i = 0
    for key in dict:
        dict[key] = cols[i].text
        i = i + 1
    amazon_dict.append(dict)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

amazon_data = pd.DataFrame(amazon_dict)
amazon_data["Date"] = pd.to_datetime(amazon_data["Date"], format="%b %d, %Y")

# Question 1, What is the content of the title attribute?
print(soup.title)

# Question 2, Print out the first five rows of the amazon_data created
print(amazon_data.head())

# Question 3, What is the open of the last row of the amazon_data dataframe
# print(amazon_data.tail(1))
print(amazon_data.iloc[60]["Open"])


# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
#
# data = requests.get(url).text
# soup = BeautifulSoup(data, "html5lib")
# table = soup.find("table")
#
# netflix_dict = []
# for row in table.find("tbody").find_all("tr"):
#     dict = {"Date": None,
#             "Open": None,
#             "High": None,
#             "Low": None,
#             "Close": None,
#             "Adj_Close": None,
#             "Volume": None}
#     cols = row.find_all("td")
#     i = 0
#     for key in dict:
#         dict[key] = cols[i].text
#         i = i + 1
#     netflix_dict.append(dict)
#
# netflix_data = pd.DataFrame(netflix_dict)
# netflix_data["Date"] = pd.to_datetime(netflix_data["Date"], format="%b %d, %Y")
# print(netflix_data.head())