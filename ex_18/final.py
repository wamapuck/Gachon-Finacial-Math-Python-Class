import requests as rq
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
import json

url = "https://jonghyup.com/tmp/random_links.php"

response = rq.get(url)
bs_pasered = bs(response.text, "html.parser")

row_number = bs_pasered.find("td", {"id":"row_number"}).text

row = bs_pasered.find_all("tr")

row_rq = []

for i in row[int(row_number)].find_all("td"):
    row_rq.append(str(i.text))

row_rq_url = json.loads(row_rq[1])

xml_req = rq.get(row_rq_url["link"]).text
root = ET.fromstring(xml_req)

print(root.find("message").text)