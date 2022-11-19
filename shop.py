import requests
# from bs4 import BeautifulSoup
import json
# import csv
# from random import randint
from time import sleep
# import re
# import pandas as pd

def parsing(slice=1):
   headers = {
      'authority': 'store.tildacdn.com',
      'accept': '*/*',
      'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
      'origin': 'https://happybagspb.ru',
      'referer': 'https://happybagspb.ru/',
      'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Linux"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
   }

   params = {
      'storepartuid': '464249294850',
      'recid': '285042057',
      'c': '1668796177968',
      'getparts': 'true',
      'getoptions': 'true',
      'slice': slice,
      'size': '36',
   }

   sleep(1)
   response = requests.get('https://store.tildacdn.com/api/getproductslist/', params=params, headers=headers)
   return response.json()

def perebor(products):
   prod_dict = {}
   for product in products:
      gallery = product.get('gallery').split('/')[-1]
      if gallery == '_.jpg"}]':
         title = product.get('title')
         url = product.get('url')
         id = product.get('uid')

         prod_dict[id] = (title, url)
   # print(prod_dict)
   return prod_dict

def products_dict():
   slice = 1
   prod_dict = {}
   while slice:  
      response = parsing(slice)
      try:
         nextslice = response.get('nextslice')
      except:
         nextslice = 0

      products = response.get('products')
      prod_dict = prod_dict | perebor(products)

      # slice = nextslice
      
      print(f'nextslice = {nextslice}')
      slice = nextslice

   # print(f'\n{prod_dict}')
   return prod_dict

def tojson():
   with open('shop.json', 'w') as file:
      json.dump(products_dict(), file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
   # tojson()
   pass
else:
   print("File one executed when imported")