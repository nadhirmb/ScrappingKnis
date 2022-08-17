
# Online Python - IDE, Editor, Compiler, Interpreter
from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.jumia.dz/mlp-telephone-tablette/smartphones/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_="prd _fb col c-prd")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h3', class_="name").text.replace('\n', '')
        price = list.find('div', class_="prc").text.replace('\n', '')

        info = [title, price ]
        thewriter.writerow(info)