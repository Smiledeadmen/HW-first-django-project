import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from .settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    CONTENT = []
    with open(BUS_STATION_CSV, encoding='cp1251') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            CONTENT.append(row)
    paginator = Paginator(CONTENT, 10)
    current_page = int(request.GET.get('page', 1))
    next_page_url = f'?page={current_page + 1}'
    pagi_data = paginator.get_page(current_page)
    return render(request, 'index.html', context={
        'bus_stations': pagi_data,
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

