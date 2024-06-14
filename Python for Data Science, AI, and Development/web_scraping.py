import requests
from bs4 import BeautifulSoup

# use the get method to retrieve html body

# create a BeautifulSoup object

# html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
# <b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
# <h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
# <h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

html = "<!DOCTYPE html><html><head><title>LoliLita</title></head><body> \
        <h3><b id='highlight'>Crystal Rabbit Jumperskirt</b></h3><p>₱ 7,200</p> \
        <h3>Mary Jane High Heel Shoes</h3><p>₱ 7,950</p><h3>Ankle Socks with Lace in Pink \
        </h3><p>₱ 500</p></body></html>"
soup = BeautifulSoup(html, "html5lib")
print(soup.prettify()) # Prints HTML nested code
print(soup.title) # <title>LoliLita</title>
print(type(soup.title)) # <class 'bs4.element.Tag'>
print(soup.h3) # will retrieve the first h3, <h3>Crystal Rabbit Jumperskirt</h3>
print(soup.h3.child) # does not have a child, None
print(soup.h3.next_sibling) # will retrieve the next h3 since it is its sibling, <h3><p>₱ 7,200</p>         </h3>
print(soup.b["id"]) # id of b tag is highlight
print(soup.b.attrs) # {'id': 'highlight'}
print(soup.b.get("id")) # highlight
print(soup.b.string) # Crystal Rabbit Jumperskirt
print(type(soup.b.string)) # <class 'bs4.element.NavigableString'>
print(type(str(soup.b.string))) # <class 'str'>

products = soup.find_all("h3")
for no, product in enumerate(products):
    no = no + 1
    print(f"{no} {str(product.string)}")

table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> \
<td>Payload mass</td></tr><tr> <td>1</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> \
<td>300 kg</td></tr><tr><td>2</td> \
<td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> \
<td>94 kg</td></tr><tr><td>3</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> \
<td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "html5lib")
print(table_bs.prettify())
table_rows = table_bs.find_all("tr")
print(table_rows[0])
print(type(table_rows[0]))

for i, row in enumerate(table_rows):
    i = i + 1
    print("row", i)
    table_cells = row.find_all("td")
    for j, cell in enumerate(table_cells):
        print(str(cell.string))

# using a list can match against any item in that list
list_input = table_bs.find_all(name=["tr", "td"])
print(list_input)

tags_with_ids = table_bs.find_all(id="flight")
print(tags_with_ids)

links_related_to_florida = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(links_related_to_florida) # expected to have 2 links related florida

print(table_bs.find_all("a", href=True)) # retrieves all anchor tags that have href attributes, expected to have 3
print(table_bs.find_all("a", href=False)) # retrieves all anchor tags that does NOT HAVE href attributes, expected to have 0
print(table_bs.find_all(string="Florida")) # retrieves strings that has the argument given to it

two_tables="<h3>Rocket Launch </h3> \
<p><table class='rocket'> \
<tr><td>Flight No</td><td>Launch site</td><td>Payload mass</td></tr> \
<tr><td>1</td><td>Florida</td><td>300 kg</td></tr> \
<tr><td>2</td><td>Texas</td><td>94 kg</td></tr> \
<tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p>\
<p><h3>Pizza Party</h3> \
<table class='pizza'> \
<tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr> \
<tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr> \
<tr><td>Little Caesars</td><td>12</td><td >144 </td></tr> \
<tr><td>Papa John's</td><td>15 </td><td>165</td></tr>"

two_tables_bs = BeautifulSoup(two_tables, "html.parser")

# Retrieving first table (find is used to just retrieve one entry)
print(two_tables_bs.find("table"))
# Retrieving table that has an id of pizza
print(two_tables_bs.find("table", class_="pizza"))
