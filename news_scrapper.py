# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import os, codecs

news_page = 'https://www.yahoo.com/news/'
page = urllib2.urlopen(news_page)
soup = BeautifulSoup(page, 'html.parser')

category = soup.find_all('div', {'data-test-locator':'catlabel'})
headline = soup.find_all('h3', class_="Mb(5px)")
headlines_list = []
for index, i in enumerate(category):
    headlines_list.append(i.text + ': ' + headline[index].text)

index = 1
news_list = []
for headline in headlines_list:
	#headline_link = headline.find('a')
	#print headline_link
	news_list.append(headline)
	index += 1

# The notifier function
def notify(title):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(' ')
    os.system('terminal-notifier {}'.format(' '.join([m, t])))

    file = codecs.open("news.html", "w", "utf-8")
    style = "<html><head><title>Today's News</title></head> <body style='background:#ededed'> <h3>Today's News</h3> <ul>"
    file.write(style)
    for headline in news_list:
    	file.write("<li>" + headline + '</li>')
    file.write("</ul> </body>")
    file.close()
    os.system("open news.html")

# Calling the function
notify(title = "Opening today's NEWS")