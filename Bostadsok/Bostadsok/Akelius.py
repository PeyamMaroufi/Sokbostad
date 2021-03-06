from bs4 import BeautifulSoup, SoupStrainer
import requests


class Akelius:
    def __init__(self):
        pass

    @staticmethod
    def akelius_items_li():
        """
            ## DESCRIPTION
            Static function

            Getting the existing items from Akelius webpage. It uses
            the beautiful library to gather all section tagged with h3
            and img. Looking for the image url and link url, gathering
            them in a list to be able to show them later. Each element
            has a link and image so no complicated algorithm is required

            The output structure is :
            akelius_items = (Link to the object, apartment's address,
                             describtion of the apartment such as flooe
                             and size, rent)
            ## ALGORITHM:
            1. Call website
            2. Catch the content
            3. Parse

            ## INPUTS:
                none

            ## OUTPUTS:
                akelius_items     - dictionary containing img url and link
                                  and title

        """
        # Local variables
        # Dictionary to collect all info
        akelius_items = {}
        # Get the source of the page
        url_list_of_apartmens = "https://rent.akelius.com/sv/search/sweden/apartment/stockholm"
        # Base url to add to the image url
        waling_base_url = "https://rent.akelius.com"
        # Gathering h3 and image addresses
        url_title_link = []
        room_size_floor = []
        rent_li = []
        address_li = []
        desc_li = []
        r1 = requests.get(url_list_of_apartmens)

        if r1.status_code == 200:

            coverpage = r1.content
            soup1 = BeautifulSoup(coverpage, 'html.parser')
            coverpage_news = soup1.find_all(
                'div', class_=['title', 'address', 'fact ng-star-inserted', 'amount'])

            for item in coverpage_news:

                if item.attrs['class'][0] == 'title':
                    title_temp = item.string
                    link_temp = item.contents[0].contents[0].attrs['href']
                    title_link_temp_dic = {
                        title_temp: waling_base_url + str(link_temp)}
                    url_title_link.append(title_link_temp_dic)

                if item.attrs['class'][0] == 'fact':
                    desc_temp = item.text
                    room_size_floor.append(desc_temp)

                if item.attrs['class'][0] == 'amount':
                    rent_temp = item.text
                    rent_li.append(rent_temp)

                if item.attrs['class'][0] == 'address':
                    addres_temp = item.text
                    address_li.append(str(addres_temp))

            for item in range(0, len(url_title_link)):
                temp_keys = list(url_title_link[item].keys())[0]
                temp_link = list(url_title_link[item].values())[0]
                rent_temp = rent_li[item]
                for desc in range(0, len(room_size_floor), 3):
                    rum_temp = room_size_floor[desc]
                    size_temp = room_size_floor[desc + 1]
                    floor_temp = room_size_floor[desc + 2]
                    desc_li.append([rum_temp, size_temp, floor_temp])
                akelius_items[temp_keys] = (
                    temp_link, address_li[item], desc_li[item], rent_temp)

        return akelius_items
