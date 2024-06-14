import requests
from bs4 import BeautifulSoup
import html5lib

# use the get method to retrieve html body

# create a BeautifulSoup object

# html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
# <b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
# <h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
# <h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

html = "<!DOCTYPE html><html><head><title>LoliLita</title></head><body> \
        <h3>Crystal Rabbit Jumperskirt<h3><p>₱ 7,200</p> \
        <h3>Mary Jane High Heel Shoes</h3><p>₱ 7,950</p><h3>Ankle Socks with Lace in Pink \
        </h3><p>₱ 500</p></body></html>"
soup = BeautifulSoup(html, "html5lib")
print(soup.prettify()) # Prints HTML nested code
print(soup.title) # <title>LoliLita</title>
print(type(soup.title)) # <class 'bs4.element.Tag'>
print(soup.h3) # will retrieve the first h3