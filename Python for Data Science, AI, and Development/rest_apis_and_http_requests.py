import requests

import os
from PIL import Image

url = "https://www.ibm.com/"
r = requests.get(url)
print(r.status_code) # 200 means successful
print(r.request.headers)
print(r.request.body)
print(r.headers)
print(r.headers["date"]) # Date when the request was done
print(r.headers["Content-Type"]) # text/html; charset=utf-8
print(r.encoding) # utf-8
print(r.text) # HTML body

url_get = "https://jsonplaceholder.typicode.com/comments"
payload = {"postId": 1}
r = requests.get(url_get, params=payload)
print(r.text)
print(r.url) # https://jsonplaceholder.typicode.com/comments?postId=1
print(r.request.body) # None because data is sent via query parameters in URL as opposed with POST
print(r.headers["Content-Type"]) # application/json; charset=utf-8
print(r.json()) # Returns a dictionary


url_post = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "Testing POST requests", "body": "Learning HTTP Requests and Response", "userId": 1}
r = requests.post(url_post, data=payload)
print(r.url) # https://jsonplaceholder.typicode.com/posts
print(r.request.body) # title=Testing+POST+requests&body=Learning+HTTP+Requests+and+Response&userId=1
print(r.json()) # Note that this payload dictionary wont return anything because there is no match found in requested server
# Furthermore, the website does not allow user to change any content there

# Retrieving image
url= 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
# Make a get request
r = requests.get(url)
# Gets information regarding about the URL
print(r.headers)
print(r.headers["Content-Type"])
# File path of the image (getcwd means get current working directory path)
path = os.path.join(os.getcwd(), "image.png")
# Save the file using write-binary mode (this mode is used because the file contains data that is not text rather we
# write the raw bytes exactly as they are to the file
with open(path, "wb") as file:
    file.write(r.content)
# View the image
Image.open(path)

# Retrieving another image
url = "https://content.dodea.edu/VS/HS/webdesign/masterz/s/module4/images/table-tag-example.gif"
r = requests.get(url)
path = os.path.join(os.getcwd(), "table-tag.example.gif")
with open(path, "wb") as file:
    file.write(r.content)
Image.open(path)

# Retrieving text file
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
r = requests.get(url)
print(r.headers)
print(r.headers["Content-Type"])
path = os.path.join(os.getcwd(), "Example1.txt")
with open(path, "wb") as file:
    file.write(r.content)

