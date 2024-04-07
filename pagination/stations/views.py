from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(rows, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'bus_stations': rows[10*(page_number-1):
                             10*page_number]
    }
    return render(request, 'stations/index.html', context)
