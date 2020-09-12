from bs4 import BeautifulSoup, SoupStrainer
import requests


class Akelius:
    def __init__(self):
        pass

    def akelius_items_li(self):
        # Local variables
        # Dictionary to collect all info
        items_walin = {}
        # Get the source of the page
        urls = "https://rent.akelius.com/sv/search/sweden/apartment/stockholm"
        # Base url to add to the image url
        base_url = "https://rent.akelius.com"
        # Gathering h3 and image addresses
        url_title_link = []
        url_adress = []

        r1 = requests.get(urls)

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
                        title_temp: base_url + str(link_temp)}
                    url_title_link.append(title_link_temp_dic)
                if item.attrs['class'][0] = 'fact ng-star-inserted':
                    pass
                if item.attrs['class'][0] = 'amount':
                    pass

                if item.attrs['class'][0] == 'address':
                    addres_temp = item.string
                    url_adress.append(str(addres_temp))

            for item in range(0, len(url_title_link)):
                temp_keys = list(url_title_link[item].keys())[0]
                temp_values = list(url_title_link[item].values())[0]
                items_walin[temp_keys] = (temp_values, url_adress[item])


a = Akelius()
a.akelius_items_li()
