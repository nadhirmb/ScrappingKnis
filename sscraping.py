
# Online Python - IDE, Editor, Compiler, Interpreter
from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.jumia.dz/telephone-tablette/"

def getdata(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def getarticles(soup):
    lists = soup.find_all('article', class_="prd _fb col c-prd")
    return lists
    

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('div', {'class': 'pg-w -ptm -pbxl'})
    if not pages.find('a', {'aria-label': 'Dernière page'}):
        url = 'https://www.amazon.co.uk' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return



with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h3', class_="name").text.replace('\n', '')
        price = list.find('div', class_="prc").text.replace('\n', '')

        info = [title, price ]
        thewriter.writerow(info)