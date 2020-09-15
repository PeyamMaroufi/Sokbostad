from bs4 import BeautifulSoup, SoupStrainer
import requests


class Hasselby:
    def __init__(self):
        pass

    def hasselby_items_li(self):
        # Local variables
        # Dictionary to collect all info
        items_hasselby = {}
        # Get the source of the page
        urls = "https://bostad.hasselbyhem.se/HSS/Object/object_list.aspx?cmguid=4e6e781e-5257-403e-b09d-7efc8edb0ac8&objectgroup=1"
        # Base url to add to the image url
        base_url = "https://bostad.hasselbyhem.se/HSS/Object/"
        r1 = requests.get(urls)

        if r1.status_code == 200:

            coverpage = r1.content
            soup1 = BeautifulSoup(coverpage, 'html.parser')
            coverpage_news = soup1.find_all(
                'td', class_=['gridcell'])

            i = 0
            while i < len(coverpage_news):
                title_str = coverpage_news[i+1].string
                link_str = coverpage_news[i+1].contents[0].attrs['href']
                address_str = coverpage_news[i+2].string
                room_str = coverpage_news[i+3].string
                size_str = coverpage_news[i+4].string
                rent_str = coverpage_news[i+5].string
                items_hasselby[title_str] = (
                    base_url + link_str, address_str, room_str, size_str, rent_str)
                i += 8

        return items_hasselby
