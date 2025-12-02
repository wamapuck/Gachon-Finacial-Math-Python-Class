import urllib.request as req
from bs4 import BeautifulSoup

url = "https://finance.naver.com/research/"
response = req.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

base_tab = soup.find_all("div", {"class": "box_type_m"})

for i in base_tab:
    print(i.find_all("td"))
    print("-" * 100)


# find_all에서 find_all 사용하는법 확인