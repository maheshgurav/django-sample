
from django.conf.urls import url
from django.contrib import admin
from common.request_router import search_hotel, add_hotel

urlpatterns = [
    url(r'^hotel-finder/add/', add_hotel),
    #url(r'^hotel-finder/update/', admin.site.urls),
    url(r'^hotel-finder/delete/', admin.site.urls),
    url(r'^hotel-finder/search/', search_hotel),
]