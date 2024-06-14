import requests
from bs4 import BeautifulSoup

url = "https://www.ibm.com/"

data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")
# print(soup.prettify()) # Retrieves an HTML code

# Scraping all links
for link in soup.find_all("a", href=True):
    print(link.get("href")) # It retrieves two links

# Scraping all images Tags
for link in soup.find_all("img"):
    print(link)
    print(link.get("src"))


# Scraping data from HTML tables
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")
table = soup.find("table")

for row in table.find_all("tr"):
    cols = row.find_all("td")