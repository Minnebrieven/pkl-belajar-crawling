import mongotor
from bs4 import BeautifulSoup as soup

def bsparsing(data,theplat):
    page_soup = soup(data, 'lxml')
    table = page_soup.find_all('tr') 
    dic = dict({"plat":theplat})
    for i in range(1, len(table) - 1):
        tds = table[i].find_all('td')
        key = tds[1].text.replace('\xa0','').replace('.','').strip()
        val = tds[2].text.replace('\xa0','').strip()
        dic[key]=val
    if dic['Jenis - Cyl / Sumbu'] == None or dic['Jenis - Cyl / Sumbu'] == '':
        print(dic['plat'],'Empty')
    else:
        print(dic['plat'],'Fill')
        return dic