# Access site, find Technology section
# For first 100 headlines, collect: headline, URL, author/source, post/edit time
# Persist collection, eliminate duplicates
# Alternate output: write to CSV file

import requests
from bs4 import BeautifulSoup

# randomize hits, to avoid blacklisting
from time import sleep
from random import randint

site = "http://www.yangtse.com/app/internet/index.html"
page = requests.get(site)
soup = BeautifulSoup(page.text, 'html.parser')

item = soup.select(".box-text-title > a")

# isolate and collect URLs for each item on page (~12 URLs)
urls = []
for a in item:
    urls.append(a["href"])

# print (urls)

while urls.count("http") < 101:
    n = 2
    j = 2
    page = requests.get("http://www.yangtse.com/app/internet/index_" + str(n) + ".html")


    # pause btwn 8-15s, monitor requests
    sleep(randint(8,15))

    print("Request no."+str(j) + ", Index page "+str(n), "urls count is "+str(urls.count("http")))
    n+=1
    j=+1

    # isolate and collect URLS for each item on list_page
    soup = BeautifulSoup(page.text, 'html.parser')
    item = soup.select(".box-text-title > a")

    for a in item:
        urls.append(a["href"])


        #Iterate through collection of URLs, extract details for 12 articles
        articles = []
        for link in urls:
            soup = BeautifulSoup(requests.get(link).text, 'html.parser')
        #collect headline, author, time, URL
            item2_headline = soup.select(".text-title")
            item2_author_time = soup.select(".text-time")
            item2_URL = link
        #persist collection
            articles.append((item2_URL, item2_headline, item2_author_time))

print(articles)
