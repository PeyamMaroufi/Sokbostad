import hashlib
from bs4 import BeautifulSoup, SoupStrainer
import requests


# Get the source of the page
urls = "https://wahlinfastigheter.se/lediga-objekt/lagenheter/"
base_url = "https://wahlinfastigheter.se"
r1 = requests.get(urls)
print(r1.status_code)
url_h3 = []
url_lazy = []
url_img = []

# Wåhlins fastighet
if r1.status_code == 200:

    coverpage = r1.content

    soup1 = BeautifulSoup(coverpage, 'html.parser')

    coverpage_news = soup1.find_all(
        ['h3', 'img'], class_=['block-title', 'lazy'])

    print(len(coverpage_news))

    for item in coverpage_news:

        if item.attrs['class'][0] == 'block-title' and (item.text not in ['\nParkering\n', '\nLokaler\n', '\nFörråd\n']):

            temp_url = item.find('a', href=True)
            url_h3.append(temp_url.attrs['href'])

        if item.name == 'img' and (item.attrs['alt'] not in ['Parkering', 'Lokaler', 'Förråd']):

    print("Slut")

    # replace out all the parts we don't need

    # calculate mds Hash

    # compare the hash with the stored hash, different? do something

    # store the new hash
