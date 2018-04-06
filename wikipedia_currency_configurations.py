from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/List_of_circulating_currencies")
handler = html.read()
soup = BeautifulSoup(handler, "html5lib")
tr = soup.find("table",{"class":"wikitable sortable"}).find_all("tr")
aDict = {}
for i in tr:
    k = i.find_all("td")
    if len(k) == 6:
        aDict[re.sub(r'\[.*\]', '', str(k[3].text).strip())] = re.sub(r'\[.*\]', '', str(k[1].text).strip())
    elif len(k) == 5:
        aDict[re.sub(r'\[.*\]', '', str(k[2].text).strip())] = re.sub(r'\[.*\]', '', str(k[0].text).strip())
		
aDict.pop("(none)", None)
finaloutput=("currencymap = {\n " + ("\n".join(",\"{}\": \"{}\"".format(k, v) for k, v in sorted(aDict.items())) + "\n}")[1:])
file = open('configurations/currency_configurations.py',mode='w',encoding='utf-8')
file.write("# -*- coding: utf-8 -*-\n")
file.write(finaloutput)
print("Updated currency_configurations")
