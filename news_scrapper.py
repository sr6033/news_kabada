# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import os, codecs

news_page = 'https://www.yahoo.com/news'
page = urllib2.urlopen(news_page)
soup = BeautifulSoup(page, 'html.parser')

headlines_list = soup.find_all('h3')

index = 1
news_list = []
urls_list = []
for headline in headlines_list:
	#headline_link = headline.find('a')
	#print headline_link
	url = headline.parent.get('href')
	if not url:
		url = headline.find('a').get('href')
	headline = headline.text.strip()
	news_list.append(headline)
	urls_list.append(news_page + url)
	index += 1

# The notifier function
def notify(title):
	t = '-title {!r}'.format(title)
	m = '-message {!r}'.format(' ')
	os.system('terminal-notifier {}'.format(' '.join([m, t])))

	file = codecs.open("news.html", "w", "utf-8")
	style = "<html><head><title>Today's News</title>\
			<link href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO\" crossorigin=\"anonymous\">\
			</head> <body style='background:#ededed'> <center><h1 style=\"padding:25px\">Today's News</h1></center><div class=\"container container-fluid main-container\" style=\"padding-bottom:25px\">"
	file.write(style)
	for i, headline in enumerate(news_list):
		file.write("<div class=\"card\" style=\"margin-bottom:10px\"><div class=\"card-body\"><a style=\"color:#020e65\" href=\"" + urls_list[i] + "\"><center>" + headline + "</center></a></div></div>")
	file.write("</div></body>")
	file.close()
	os.system("open news.html")

# Calling the function
notify(title = "Opening today's NEWS")