# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

def line ():
    print (40*'-')

wiki_link = 'https://ru.wikipedia.org/wiki/'
autor_name = 'Кир_Булычёв'


print('start')
adress = requests.get(wiki_link+autor_name)
print(wiki_link+autor_name)

soup = BeautifulSoup(adress.content, 'html.parser')
autor = soup.find(id="mw-content-text")                    #здесь биография
autor_data = soup.find('table', class_="infobox vcard")    #здесь общие даты
# print(autor_data)

for i in autor:
    folder_name = (i.get_text())
    print(folder_name)
    line()