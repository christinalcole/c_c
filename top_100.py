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

print(item)
