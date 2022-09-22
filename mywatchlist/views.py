from django.shortcuts import render
from multiprocessing import context
from operator import truediv
from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    mywatchlist_data = WatchList.objects.all()

    watched_number = 0
    unwatched_number = 0
    message = ""

    for x in mywatchlist_data:
        if x.watched == True:
            watched_number+=1
        else :
            unwatched_number+=1
    if watched_number >= unwatched_number :
        message = ("Congratulations, you have watched a lot of movies!")
    else :
        message = ("Woah, you need to watch more movies!")

    context = {
        'mywatchlist_list': mywatchlist_data,
        'nama': 'Muhammad Fiqo Anugrah',
        'id': '2106657286',
        'message': message
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_xml = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

def show_json(request):
    data_json = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

def show_json_id(request, id):
    data_json_id = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_json_id), content_type="application/json")

def show_xml_id(request, id):
    data_xml_id = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_xml_id), content_type="application/xml")
