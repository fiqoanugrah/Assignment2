from django.urls import path
from mywatchlist.views import show_mywatchlist

app_name = 'mywatchlist'
urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
]