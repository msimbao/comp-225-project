def lol():
  print("hey")

import os
from flask import Flask, request, render_template, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib.request, urllib.error
import random
import socket  

"""
Code From Jack's file
All the functions can be used in server.py to edit incoming data
We import it into server.py at the top along with other necessary modules
Extra modules are installed throught the terminal and listed in requirements.text
"""

def getPageSource(baseurl):
    datalist = []
    html = askURL(baseurl)
    bs = BeautifulSoup(html, 'html.parser')
    return bs

def getParagraphs(baseurl):
    paraGraphlist = []
    bs = getPageSource(baseurl)
    for item in bs.find_all('p'):
        item = str(item)
        paraGraphlist.append(item)
    return paraGraphlist

def findUrls(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def saveTxt(my_list):
    with open('.\\lianyungang.txt', 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)


def main():
    baseurl = "https://www.mlb.com/"
    Mookie_or_Soto = "https://www.mlb.com/news/mookie-betts-or-juan-soto-for-best-right-fielder"
    print(getParagraphs(Mookie_or_Soto))

main()
