from Walin import Walin
from Hasselby import Hasselby
from WasbyHem import WasbyHem
from Akelius import Akelius
from Heba import Heba
import argparse

"""
## DESCRIPTION
This file is only use to call each module and print out
the results."""


def walin_items():
    x = 0
    items = Walin.walin_items_li()
    while items[x] is not None:
        yield items[x].items()
        x += 1


def hasselby_items():
    x = 0
    items = Hasselby.hasselby_items_li()
    while items[x] is not None:
        yield items[x].items()
        x += 1


def wasbyhem_items():
    x = 0
    items = WasbyHem.wasby_items_li()
    while items[x] is not None:
        yield items[x].items()
        x += 1


def akelius_items():
    x = 0
    items = Akelius.akelius_items_li()
    while items[x] is not None:
        yield items[x].items()
        x += 1


def heba_items():
    x = 0
    items = Heba.heba_items_li()
    while items[x] is not None:
        yield items[x].items()
        x += 1


def printAllApartment():
    for item in walin_items():
        print(item)


def main():
    parser = argparse.ArgumentParser(
        description='Print information on available housings.')
    parser.add_argument(
        "-a", "--all", help="List of all available housings from all hosts", required=False, dest="all_apartments", default=False)
    parser.add_argument(
        "-l", help="Show apartments from a specified host\n\tHosts:\n\tHeba\n\tHasselbyhem\n\tWaling\n\tWasbyhem\n\tAkelius", required=False, dest="host_var", type=str)
    arguments = parser.parse_args()
    all_apartments = arguments.all_apartments
    host_var = arguments.host_var

    if all_apartments:
        print("hi")
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
    main()
