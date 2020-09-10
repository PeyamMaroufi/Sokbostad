import hashlib
from bs4 import BeautifulSoup, SoupStrainer
import requests

items_walin = {}


def walin_items_li():

    # Get the source of the page
    urls = "https://wahlinfastigheter.se/lediga-objekt/lagenheter/"
    base_url = "https://wahlinfastigheter.se"
    r1 = requests.get(urls)
    print(r1.status_code)
    url_h3 = []
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
                temp_url_desc = {temp_url.get_text(): (temp_url.attrs['href'])}
                url_h3.append(temp_url_desc)

            if item.name == 'img' and (item.attrs['alt'] not in ['Parkering', 'Lokaler', 'Förråd']):
                url_img.append(base_url + item.attrs['data-src'])

            # replace out all the parts we don't need
        for item in range(0, len(url_h3)):
            temp_keys = list(url_h3[item].keys())[0]
            temp_values = list(url_h3[item].values())[0]
            items_walin[temp_keys + ' ' +
                        str(item + 1)] = (temp_values, url_img[item])

        for key, value in items_walin.items():
            print(key)
            print(value)
            print('------')
            # calculate mds Hash

            # compare the hash with the stored hash, different? do something

            # store the new hash
walin_items_li()
