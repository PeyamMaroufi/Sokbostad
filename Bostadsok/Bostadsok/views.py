from django.shortcuts import render
from . import Walin, WasbyHem, Heba, Hasselby, Akelius


def index(request):
    return render(request, "index.html", {
        "walin": get_walin(),
        "akellius": get_akellius(),
        "hasselby": get_hasselby(),
        "heba": get_heba(),
        "wasbyhem": get_wasbyhem()
    })


def get_walin():
    return Walin.Walin.walin_items_li()


def get_akellius():
    return Akelius.Akelius.akelius_items_li()


def get_hasselby():
    return Hasselby.Hasselby.hasselby_items_li()


def get_heba():
    return Heba.Heba.heba_items_li()


def get_wasbyhem():
    return WasbyHem.WasbyHem.wasby_items_li()
