from bs4 import BeautifulSoup, SoupStrainer
import requests


class Hasselby:
    def __init__(self):
        pass

    @staticmethod
    def hasselby_items_li():
        """
            ## DESCRIPTION
            Static function

            Getting the existing items from Hässelby webpage. It uses
            the beautiful library to gather all section tagged with h3
            and img. Looking for the image url and link url, gathering
            them in a list to be able to show them later. Each element
            has a link and image so no complicated algorithm is required

            hasselby_items = (Link to the apartment
                              address of the apartment,
                              number of rooms,
                              size of the apartment,
                              rent of the apartment)

            ## ALGORITHM:
            1. Call website
            2. Catch the content
            3. Parse

            ## INPUT:
                none
            ## OUTPUT:
                hasselby_items     - dictionary containing img url and link
                                     and title
        """
        # Local variables
        # Dictionary to collect all info
        hasselby_items = {}
        # Get the source of the page
        url_list_of_apartmens = "https://bostad.hasselbyhem.se/HSS/Object/object_list.aspx?cmguid=4e6e781e-5257-403e-b09d-7efc8edb0ac8&objectgroup=1"
        # Base url to add to the image url
        hasselby_base_url = "https://bostad.hasselbyhem.se/HSS/Object/"
        r1 = requests.get(url_list_of_apartmens)

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
                hasselby_items[title_str] = (
                    hasselby_base_url + link_str, address_str, room_str, size_str, rent_str)
                i += 8
        return hasselby_items
