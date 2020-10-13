from bs4 import BeautifulSoup, SoupStrainer
import requests


class WasbyHem:
    def __init__(self):
        pass

    @staticmethod
    def wasby_items_li():
        """
            Getting the existing items from WäsbyHem webpage. It uses
            the beautiful library to gather all section tagged with h3
            and img. Looking for the image url and link url, gathering
            them in a list to be able to show them later. Each element
            has a link and image so no complicated algorithm is required

            Algorithm:
            1. Call website
            2. Catch the content
            3. Parse

            input:
                none
            output:
                wasby_hem     - dictionary containing img url and link
                                  and title
        """
        # Local variables
        # Dictionary to collect all info
        wasby_hem = {}
        # Get the source of the page
        urls = "https://www.vasbyhem.se/ledigt/lagenhet"
        # Base url to add to the image url
        base_url = "https://www.vasbyhem.se/ledigt/"
        r1 = requests.get(urls)

        if r1.status_code == 200:

            coverpage = r1.content
            soup1 = BeautifulSoup(coverpage, 'html.parser')
            coverpage_news = soup1.find_all(
                'td', class_=['gridcell'])

            i = 0
            while i < len(coverpage_news):
                title_str = coverpage_news[i+2].string
                link_str = coverpage_news[i+2].contents[0].attrs['href']
                address_str = coverpage_news[i+2].string
                room_str = coverpage_news[i+4].string
                size_str = coverpage_news[i+5].string
                rent_str = coverpage_news[i+7].string
                wasby_hem[title_str] = (
                    base_url + link_str, address_str, room_str, size_str, rent_str)
                i += 10

        return wasby_hem
