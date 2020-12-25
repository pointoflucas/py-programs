import sys
sys.path.append("C:/Users/Mustafa/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/site-packages")
import requests
from bs4 import BeautifulSoup

URL = "https://www.alibaba.com/product-detail/Frameless-23-8-Inch-all-in_62576626041.html?spm=a2700.galleryofferlist.topad_creative.d_image.49ce3245F2BEV7&fullFirstScreen=true"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('title')
price = soup.find("div", {"class":"ma-spec-price ma-price-promotion"}).find("span", {"class":"priceVal"})
converted_price = float(price.string[1:5])
print(title.string)
print(converted_price)

if converted_price<250:
    send_notification()

#In this project, BeautifulSoup and bs4 are used !!!





