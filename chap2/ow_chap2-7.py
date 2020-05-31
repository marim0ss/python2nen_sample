#coding: UTF-8
import requests
from bs4 import BeautifulSoup
import pprint

# Webページを取得して解析する
load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url).text
soup = BeautifulSoup(html, "html.parser")

main_topic_path = "div.topicsList ul li a"  # #contentsWrap > section > div > div > div > ul

topics = soup.select(main_topic_path)

for topic in topics:
	print(topic.get("href"))
	print(topic.text)
