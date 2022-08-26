from bs4 import BeautifulSoup
import requests
from csv import writer

with open('pricesFromJumia.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  header = ['Name', 'Price']
  thewriter.writerow(header)

  for page in range(1,51):
    url = "https://www.jumia.co.ke/all-products/" + "?page=" +str(page)+"#catalog-listing"
    furl = requests.get(url)
    jsoup = BeautifulSoup(furl.content , 'html.parser')
    products = jsoup.find_all('div' , class_ = 'info')

    for product in products:
      Name = product.find('h3' , class_="name").text.replace('\n', '')
      Price = product.find('div' , class_= "prc").text.replace('\n', '')
      try:
        Rating = product.find('div', class_='stars _s').text.replace('\n', '')
      except:
        Rating = 'None'

      info = [ Name, Price]
      thewriter.writerow(info)
