# Access site, find Technology section
# For first 100 headlines, collect: headline, URL, author/source, post/edit time
# Persist collection, eliminate duplicates
# Alternate output: write to CSV file

import requests
from bs4 import BeautifulSoup

site = "http://www.yangtse.com/app/internet/index.html"
page = requests.get(site)
soup = BeautifulSoup(page.text, 'html.parser')

item = soup.select(".box-text-title > a")

# isolate and collect URLs for each item on page (~12 URLs)
urls = []
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
