from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)

data_katalog_item = CatalogItem.objects.all()
context = {
    'list_item' : data_katalog_item,
    'name': 'Muhammad Fiqo Anugrah',
    'NPM' : '2106657286'
}
