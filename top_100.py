# Access site, find Technology section
# For first 100 headlines, collect: headline, URL, author/source, post/edit time
# Persist collection, eliminate duplicates
# Alternate output: write to CSV file

import code
import time

import requests
from bs4 import BeautifulSoup
import csv

# randomize hits, to avoid blacklisting
from time import sleep
from random import randint

start_time = time.time()

site = "http://www.yangtse.com/app/internet/index.html"
page = requests.get(site)
# page.encoding = "GBK"
soup = BeautifulSoup(page.text, 'lxml')
# soup = BeautifulSoup(open("/Users/christinacole/Desktop/Technology - Yangtze Evening News Network.htm"), "lxml")
# soup.encoding = "GBK"
# code.interact(local=dict(globals(), **locals()))
item = soup.select(".box-text-title > a")

# isolate and collect URLs for each item on page (~12 URLs)
urls = []
for a in item:
    urls.append(a["href"])

articles = []
for link in urls:
    soup = BeautifulSoup(requests.get(link).text, 'lxml')
#collect headline, author, time, URL
    # code.interact(local=dict(globals(), **locals()))
    item2_headline = soup.select(".text-title")
    item2_author_time = soup.select(".text-time")
    item2_URL = link
#persist collection
    articles.append((item2_URL, item2_headline, item2_author_time))

print(articles)

# print(urls)
print ("--- %s seconds ---" % (time.time() - start_time))

# while len(urls) < 100:
#     n = 2
#     j = 2
#     page = requests.get("http://www.yangtse.com/app/internet/index_" + str(n) + ".html")
#
#
#     # pause btwn 8-15s, monitor requests
#     sleep(randint(8,15))
#
#     print("Request no."+str(j) + ", Index page "+str(n), "urls count is "+str(len(urls)))
#     n+=1
#     j=+1
#
#     # isolate and collect URLS for each item on list_page
#     soup = BeautifulSoup(page.text, 'lxml')
#     item = soup.select(".box-text-title > a")
#
#     #check this loop again--is it slow, or getting stuck?
#     for a in item:
#         while len(urls) < 100:
#             urls.append(a["href"])
#
#         #Iterate through collection of URLs, extract details for 12 articles
#         articles = []
#         for link in urls:
#             soup = BeautifulSoup(requests.get(link).text, 'lxml')
#         #collect headline, author, time, URL
#             item2_headline = soup.select(".text-title")
#             item2_author_time = soup.select(".text-time")
#             item2_URL = link
#         #persist collection
#             articles.append((item2_URL, item2_headline, item2_author_time))
#
# print(articles)
#
# #Option for output to CSV file
# with open('articles.csv', 'a') as csv_file:
#     writer=csv.writer(csv_file)
#     for item2_URL, item2_headline, item2_author_time in articles:
#         writer.writerow([item2_URL, item2_headline, item2_author_time])
