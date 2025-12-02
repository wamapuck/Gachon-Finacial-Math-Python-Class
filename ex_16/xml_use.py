from urllib.request import urlopen
import xml.etree.ElementTree as ET

smaple_url = "https://jonghyup.com/tmp/books.xml"

req = urlopen(smaple_url)
tree = ET.parse(req)
root = tree.getroot()

cycle = 0

for i in root:
    print(f"Book ID: {i.attrib['id']}")
    print(f"Title: {i.find('title').text}")
    for j in root[cycle].findall("author"):
        print(f"Author: {j[0].text} ({j[1].text})")
    
    print(f"Published: {i.find('published').text}")
    cycle += 1
    
    print("-"*20)
