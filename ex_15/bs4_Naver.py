from urllib.request import urlopen
from bs4 import BeautifulSoup

#contentarea_left > div:nth-child(3) > table > tbody
html_doc = "https://finance.naver.com/research/"
response = urlopen(html_doc)
soup = BeautifulSoup(response , "html.parser")
tab = soup.find("table", {"summary": "산업분석 리포트 리스트"})
for i in tab.find_all("tr")[2:8]:
    print(i.find_all("td")[2].get_text(), i.find("a").get_text(), i. find("td", {"class":"date"}).get_text().strip())