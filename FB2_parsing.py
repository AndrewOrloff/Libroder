# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup


def getBatchNameFromXml(XML_path):
    try:
        tree = ET.parse(XML_path)
        importSession = tree.getroot()
        batches = importSession.findall('book-title')
        # batch = batches.attrib
        # name = batch.get('book-title')
        print(batches)
        # print(batch)
        # print(name)

    except IOError as e:
        print(e)

def line():
    print ('-'*20)

print('start')

path_to_fb2 = 'd:/Users/Andrew/PycharmProjects/Libroder/FB2_test/'
files_list = os.listdir(path_to_fb2)

line()
for i in files_list:
    print (i)
line()

print('parse path:', path_to_fb2 + files_list[2])
print('parse file:', files_list[2])

adress = requests.get(path_to_fb2 + files_list[2])
soup = BeautifulSoup(adress.content, 'fb2.parser')
autor = soup.find('autor')
print('autor:', autor)

tree = ET.parse(path_to_XML + files_list[2])
root = tree.getroot()
getBatchNameFromXml(path_to_XML + files_list[2])

line()

print('ROOT:', root)
print('Корневой элемент:', root.tag)
print('Длинна корня:', len(root))

i=0
for child in root:
    line()
    print(child.tag)
    print(child.attrib)
    print(root[i].tag)
    print(root[i].attrib)
    i +=1
line()
print(root[i].getchildren())

print('Parsing DONE')