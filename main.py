import hashlib
from bs4 import BeautifulSoup, SoupStrainer
import requests


# Get the source of the page
urls = "https://wahlinfastigheter.se/lediga-objekt/lagenheter/"
r1 = requests.get(urls)
print(r1.status_code)


# Wåhlins fastighet
if r1.status_code == 200:
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all(
        ['h3', 'span'], class_=['block-title', 'data'])
    print(len(coverpage_news))
    # print(coverpage_news)
    for item in coverpage_news:
        if item.name == 'span':
            print('Data: ' + item.get_text())
    # print(coverpage_news[0].get_text())


# replace out all the parts we don't need

# calculate mds Hash


# compare the hash with the stored hash, different? do something

# store the new hash
