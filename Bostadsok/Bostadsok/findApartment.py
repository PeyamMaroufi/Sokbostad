import argparse
import concurrent.futures
import time
import os
import sys

absPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(absPath)

from Heba import Heba
from Akelius import Akelius
from WasbyHem import WasbyHem
from Hasselby import Hasselby
from Walin import Walin

"""
# DESCRIPTION
This file is only use to call each module and print out
the results."""


def choose_host(host_variable):
    if host_variable == 0:
        items1 = list(Walin.walin_items_li().items())
        printAllApartment(items1)
    elif host_variable == 1:
        items2 = list(Akelius.akelius_items_li().items())
        printAllApartment(items2)
    elif host_variable == 2:
        items3 = list(WasbyHem.wasby_items_li().items())
        printAllApartment(items3)
    elif host_variable == 3:
        items4 = list(Heba.heba_items_li().items())
        printAllApartment(items4)
    elif host_variable == 4:
        items5 = list(Hasselby.hasselby_items_li().items())
        printAllApartment(items5)


def printTable():
    # HElp variables
    Description = "Description"
    Host = "Host"
    Rooms = "Rooms"
    Size = "Size"
    print("--------------------------------------------------------------------------------------")
    print(f"{Description:{25}}{Host:{25}}{Rooms:{10}}{Size:{10}}Rent")
    print("--------------------------------------------------------------------------------------")


def printAllApartment(items):
    # print each item from all hosts
    for d in items:
        description = d[0][0:14]
        start_string_page = d[1][0][d[1][0].find('/')+2:]
        end_string_page = start_string_page[:start_string_page.find('/')]
        if 'wahlinfastigheter' in end_string_page:
            rooms, size, rent = reformatLists(0, d)

        elif 'akelius' in end_string_page:
            description = description.lstrip()
            rooms, size, rent = reformatLists(1, d)

        else:
            rooms, size, rent = reformatLists(2, d)
        printApartmentsHelpFunction(
            description, end_string_page, rooms, size, rent)


def reformatLists(host, i):
    # Wåhlin fastigheter
    if host == 0:
        rooms = i[1][1].lstrip()
        rooms = rooms.replace("rok", "") if "rok" in rooms else rooms
        rooms = rooms.replace(" ", "")
        size = i[1][2].lstrip()
        size = size.replace("kvm", "") if "kvm" in size else size
        rent = i[1][4].lstrip()
        rent = rent.replace("kr/mån", "") if "kr/mån" in rent else rent
        rent = rent.replace("ad", "") if "ad" in rent else rent
    # Akelius fastigheter
    elif host == 1:
        rooms = i[1][2][0].lstrip()
        rooms = rooms.replace("rum", "") if "rum" in rooms else rooms
        rooms = rooms.replace(" ", "") if " " in rooms else rooms
        size = i[1][2][1].lstrip()
        size = size.replace("m²", "") if "m²" in size else size
        rent = i[1][3].lstrip()
        rent = rent.replace("SEK", "") if "SEK" in rent else rent
        rent = rent.replace(" ", "") if " " in rent else rent
    # Other hosts
    else:
        rooms = i[1][2].lstrip()
        size = i[1][3].lstrip()
        rent = i[1][4].lstrip()
        rent = rent.replace("Â", "") if "Â" in rent else rent

    return rooms, size, rent


def printApartmentsHelpFunction(description, end_string_page, rooms, size, rent):
    print(f"{description:20}{end_string_page:30}{rooms:10}{size:10}{rent}")


def main():
    parser = argparse.ArgumentParser(
        description='Print information on available housings.')
    parser.add_argument(
        "-a", help="List of all available housings from all hosts", required=False, dest="all_apartments",  default=None, action='store_true')
    parser.add_argument(
        "-l", help="Show apartments from a specified host:\n0. Wåhlin\n1. Akelius\n2. Wäsby\n3. Heba\n4. Hässelby", required=False, dest="host_integer", type=int)
    parser.add_argument(
        "-y", help="Continuously output apartments from all hosts:\n0. Wåhlin\n1. Akelius\n2. Wäsby\n3. Heba\n4. Hässelby", required=False, dest="yes_integer", type=int)

    arguments = parser.parse_args()
    all_apartments = arguments.all_apartments
    host_var = arguments.host_integer
    yes = arguments.yes_integer

    if all_apartments:
        hosts = [0, 1, 2, 3, 4]
        printTable()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = [executor.submit(choose_host, host) for host in hosts]
            for future in concurrent.futures.as_completed(threads):
                try:
                    _ = future.result()
                except Exception as exc:
                    print('Generated a stupid exception: %s' % (exc))

    if host_var is not None:
        if host_var >= 0 and host_var < 5:
            printTable()
            choose_host(host_var)
        else:
            print(
                "The host you provided does not exist. Enter en integer between [0-4] from:\n0. Wåhlin\n1. Akelius\n2. Wäsby\n3. Heba\n4. Hässelby")

    if yes is not None:
        hosts = [0, 1, 2, 3, 4]
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                printTable()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    threads = [executor.submit(choose_host, host)
                               for host in hosts]
                    for future in concurrent.futures.as_completed(threads):
                        try:
                            _ = future.result()
                        except Exception as exc:
                            print('Generated a stupid exception: %s' % (exc))
                    del concurrent.futures.thread._threads_queues[list(executor._threads)[
                        0]]
                    time.sleep(yes)
        except KeyboardInterrupt:
            exit()


if __name__ == '__main__':
    main()
