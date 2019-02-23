# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET

def getBatchNameFromXml(XML_path):
    try:
        tree = ET.parse(XML_path)
        importSession = tree.getroot()
        batches = importSession.find('<book-title>')
        # batch = batches.attrib
        # name = batch.get('book-title')
        print('fn+++', batches)
        # print(batch)
        # print(name)

    except IOError as e:
        print(e)

def line():
    print ('-'*20)

print('start')

path_to_XML = 'd:/Users/Andrew/PycharmProjects/Libroder/FB2_test/'
files_list = os.listdir(path_to_XML)


line()
for i in files_list:
    print (i)
line()

print('parse path:', path_to_XML + files_list[2])
print('parse file:', files_list[2])

tree = ET.parse(path_to_XML + files_list[2])
root = tree.getroot()
getBatchNameFromXml(path_to_XML + files_list[2])

line()

print('ROOT:', root)
print('Корневой элемент:', root.tag)
print('Длинна корня:', len(root))
print(root[2][3].text)

i=0
for child in root:
    line()
    print(root[i].tag)
    print(root[i].attrib)
    print(root[i].keys())
    print(root[i].items())
    print('text:  ', root[i].text)
    i +=1
line()

print('Parsing DONE')