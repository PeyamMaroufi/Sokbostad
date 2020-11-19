from bs4 import BeautifulSoup, SoupStrainer
import requests


class Walin:

    def __init__(self):
        pass

    @staticmethod
    def walin_items_li():
        """
            ## DESCRIPOTION
            Static function

            Getting the existing items from walin webpage. It uses
            the beautiful library to gather all section tagged with h3
            and img. Looking for the image url and link url, gathering
            them in a list to be able to show them later. Each element
            has a link and image so no complicated algorithm is required

            walin_items = (Link to the apartment, Number of rooms,
                          Size, Floor, Rent)

            ## ALGORITHM
            1. Call website
            2. Catch the content
            3. Parse
            4. Look up h3,img with conditions

            ## INPUTS
                none
            ## OUTPUTS
                walin_items     - Dictionary containing link, rooms, size
                                  floor and rent
            """

        walin_items = {}
        # Get the source of the page
        waling_base_url = "https://wahlinfastigheter.se/lediga-objekt/lagenheter/"
        # Base url to add to the image url
        url_list_of_apartmens = "https://wahlinfastigheter.se"
        # Calling the website
        r1 = requests.get(waling_base_url)

        # If the request was succesful then go on
        if r1.status_code == 200:

            coverpage = r1.content
            soup1 = BeautifulSoup(coverpage, 'html.parser')
            coverpage_news = soup1.find_all(
                ['h3'], class_='block-title')

            for item in coverpage_news:

                if item.attrs['class'][0] == 'block-title' and (item.text not in ['\nParkering\n', '\nLokaler\n', '\nFörråd\n']):

                    # Text and discribtion of the apartment
                    temp_url = item.find('a', href=True)
                    name = temp_url.text
                    name_link = temp_url.attrs['href']

                    # Go to the link of the partment to get more information
                    r2 = requests.get(name_link)
                    coverpage2 = r2.content
                    soup2 = BeautifulSoup(coverpage2, 'html.parser')
                    coverpage_link = soup2.find_all(
                        ['span'], class_='data')

                    # pick only rok, size and rent
                    rok = coverpage_link[3].text
                    size = coverpage_link[4].text
                    floor = coverpage_link[5].text
                    rent = coverpage_link[7].text

                    # Gather all information
                    walin_items[name] = [name_link, rok, size, floor, rent]

        return walin_items
