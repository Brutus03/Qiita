#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# スクレイピングに必要なモジュールをインポート
import urllib.request as req
import sys
sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')
from bs4 import BeautifulSoup
import time
import re

num = 1

# Organization一覧のurlを取得する関数
def urlget():
    url = "https://qiita.com/organizations?page="
    res = req.urlopen(url+str(num))
    data = res.read()
    text = data.decode("utf-8")
    soup = BeautifulSoup(text, "lxml") 
    org = soup.find_all(href=re.compile(r"^/organizations/"))
    for list in org:
        co = list.string
        href = list.attrs["href"]
        if co != None:
            print(co, "," "https://qiita.com"+href)

# 最後のページまでループ
while num < 30:
    urlget()
    num += 1
    time.sleep(1)
