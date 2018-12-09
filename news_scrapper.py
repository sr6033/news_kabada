# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import os, codecs
import re

news_page = 'https://www.yahoo.com/news/'
page = urllib2.urlopen(news_page)
soup = BeautifulSoup(page, 'html.parser')

headlines_list = soup.find_all('h3')

index = 1
news_list = []
news_list_dict = {}
for headline in headlines_list:
    #headline_link = headline.find('a')
    #print headline_link
    headline = headline.text.strip()
    news_list.append(headline)
    index += 1

def url_links(news_list):
    news_regex = re.compile("^\/news")
    headlines_list = soup.find_all('a', attrs={'href': news_regex})

    for headlines in headlines_list:
        news_url = headlines.get('href')
        for news in news_list:   
            if headlines.text == news: 
                news_list_dict[headlines.text] = news_page + news_url
    

# The notifier function
def notify(title):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(' ')
    os.system('terminal-notifier {}'.format(' '.join([m, t])))

    file = codecs.open("news.html", "w", "utf-8")
    style = '''
		<html>
		<head>
		<title>
		Today's News
		</title>
		<!--Beautification-->

		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
		<link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>
		<style>
		.list-group {
		font-family: 'Ubuntu Mono';font-size: 22px;
		}

		#heading{
		font-family: 'Ubuntu';
		}

		</style>
		</head>
		<body style='background:#353434'>
		<h1 class="jumbotron" id="heading">
		<center>Today's News</center>
		</h1>
		<div class="container-fluid">
        <ul class="list-group">'''
    file.write(style)
    for headline, url in news_list_dict.iteritems():
         file.write('<li class="list-group-item"> <a href="' 
                + url
                + '" target="_blank">' 
                + headline 
                + '</a></li>')
    file.write("</ul> </body>")
    file.close()
    #os.system("open news.html")
    webbrowser.open_new_tab("news.html") ## Opens the generated file in new tab


        
# Calling the function
notify(title = "Opening today's NEWS")
