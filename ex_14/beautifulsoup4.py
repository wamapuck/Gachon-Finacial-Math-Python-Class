from urllib.request import urlopen
from bs4 import BeautifulSoup

html_doc = "http://finance.naver.com/marketindex/?tabSel=gold#tab_section"
response = urlopen(html_doc)
soup = BeautifulSoup(response , "html.parser")
tab = soup.find("table", {"summary": "귀금속 리스트"})

print(tab.find("td", {"class": "num"}))

