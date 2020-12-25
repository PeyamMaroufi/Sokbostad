from Walin import Walin
from Hasselby import Hasselby
from WasbyHem import WasbyHem
from Akelius import Akelius
from Heba import Heba
import argparse

"""
# DESCRIPTION
This file is only use to call each module and print out
the results."""


def walin_items(host_variable):
    x = 0
    if host_variable == 0:
        items = Hasselby.hasselby_items_li()
    if host_variable == 1:
        items = WasbyHem.wasby_items_li()
    if host_variable == 2:
        items = Akelius.akelius_items_li()
    if host_variable == 3:
        items = Heba.heba_items_li()
    if host_variable == 4:
        items = Walin.walin_items_li()

    while items[x] is not None:
        yield items[x].items()
        x += 1


def printAllApartment():

    items = [list(Walin.walin_items_li().items()),
             list(Walin.walin_items_li().items()),
             list(Hasselby.hasselby_items_li().items()),
             list(WasbyHem.wasby_items_li().items()),
             list(Akelius.akelius_items_li().items()),
             list(Heba.heba_items_li().items())]
    Description = "Description"
    Host = "Host"
    Rooms = "Rooms"
    Size = "Size"
    print("--------------------------------------------------------------------------------------")
    print(f"{Description:{25}}{Host:{25}}{Rooms:{10}}{Size:{10}}Rent")
    print("--------------------------------------------------------------------------------------")
    for item in items:
        for i in item:
            description = i[0][0:14]
            start_string_page = i[1][0][i[1][0].find('/')+2:]
            end_string_page = start_string_page[:start_string_page.find('/')]
            if 'wahlinfastigheter' in end_string_page:
                rooms = i[1][1].lstrip()
                rooms = rooms.replace("rok", "") if "rok" in rooms else rooms
                rooms = rooms.replace(" ", "")
                size = i[1][2].lstrip()
                size = size.replace("kvm", "") if "kvm" in size else size
                rent = i[1][4].lstrip()
                rent = rent.replace("kr/mån", "") if "kr/mån" in rent else rent
                rent = rent.replace(
                    "ad", "") if "ad" in rent else rent

            elif 'akelius' in end_string_page:
                description = description.lstrip()
                rooms = i[1][2][0].lstrip()
                rooms = rooms.replace("rum", "") if "rum" in rooms else rooms
                rooms = rooms.replace(" ", "") if " " in rooms else rooms
                size = i[1][2][1].lstrip()
                size = size.replace("m²", "") if "m²" in size else size
                rent = i[1][3].lstrip()
                rent = rent.replace("SEK", "") if "SEK" in rent else rent
                rent = rent.replace(" ", "") if " " in rent else rent
            else:
                rooms = i[1][2].lstrip()
                size = i[1][3].lstrip()
                rent = i[1][4].lstrip()
                rent = rent.replace("Â", "") if "Â" in rent else rent
            print(
                f"{description:20}{end_string_page:30}{rooms:10}{size:10}{rent}")


def main():
    parser = argparse.ArgumentParser(
        description='Print information on available housings.')
    parser.add_argument(
        "-a", help="List of all available housings from all hosts", required=False, dest="all_apartments", default=False)
    parser.add_argument(
        "-l", help="Show apartments from a specified host\n\tHosts:\n\tHeba\n\tHasselbyhem\n\tWaling\n\tWasbyhem\n\tAkelius", required=False, dest="host_var", type=str)
    parser.add_argument(
        "-y", help="Continuously output apartments from all hosts\n\tHosts:\n\tHeba\n\tHasselbyhem\n\tWaling\n\tWasbyhem\n\tAkelius", required=False, dest="output_yes", type=str)

    arguments = parser.parse_args()
    all_apartments = arguments.all_apartments
    host_var = arguments.host_var
    output_yes = arguments.output_yes

    if all_apartments:
        printAllApartment()

    if host_var is not None:
        host_var = host_var.lower()
        if host_var == 'akelius':
            pass
        if host_var == 'hasselby':
            pass
        if host_var == 'wasbyhem':
            pass
        if host_var == 'waling':
            pass
        if host_var == 'heba':
            pass


if __name__ == '__main__':
    # main()
    printAllApartment()
