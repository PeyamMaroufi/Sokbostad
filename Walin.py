from bs4 import BeautifulSoup, SoupStrainer
import requests


class Waling:

    def __init__(self):
        pass

    def walin_items_li(self):
        """
            Getting the existing items from walin webpage. It uses
            the beautiful library to gather all section tagged with h3
            and img. Looking for the image url and link url, gathering
            them in a list to be able to show them later. Each element
            has a link and image so no complicated algorithm is required

            Algorithm:
            1. Call website
            2. Catch the content
            3. Parse
            4. Look up h3,img with conditions

            input:
                none
            output:
                items_walin     - dictionary containing img url and link
                                  and title
            """

        # Local variables
        # Dictionary to collect all info
        items_walin = {}
        # Get the source of the page
        urls = "https://wahlinfastigheter.se/lediga-objekt/lagenheter/"
        # Base url to add to the image url
        base_url = "https://wahlinfastigheter.se"
        # Gathering h3 and image addresses
        url_h3 = []
        url_img = []

        # Calling the website
        r1 = requests.get(urls)
        # If the request was succesful then go on
        if r1.status_code == 200:

                coverpage = r1.content
                soup1 = BeautifulSoup(coverpage, 'html.parser')
                coverpage_news = soup1.find_all(
                    ['h3', 'img'], class_=['block-title', 'lazy'])

                for item in coverpage_news:

                    if item.attrs['class'][0] == 'block-title' and (item.text not in ['\nParkering\n', '\nLokaler\n', '\nFörråd\n']):

                        temp_url = item.find('a', href=True)
                        temp_url_desc = {temp_url.get_text(): (
                            temp_url.attrs['href'])}
                        url_h3.append(temp_url_desc)

                    if item.name == 'img' and (item.attrs['alt'] not in ['Parkering', 'Lokaler', 'Förråd']):
                        url_img.append(base_url + item.attrs['data-src'])

                # replace out all the parts we don't need
                for item in range(0, len(url_h3)):
                    temp_keys = list(url_h3[item].keys())[0]
                    temp_values = list(url_h3[item].values())[0]
                    items_walin[temp_keys + ' ' +
                                str(item + 1)] = (temp_values, url_img[item])

            return items_walin
