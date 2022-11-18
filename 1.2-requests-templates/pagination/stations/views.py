from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        bus_stations_list = list(csv.DictReader(csvfile))
    paginator = Paginator(bus_stations_list, 10)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    context = {
        'bus_stations': page_obj,
        'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
