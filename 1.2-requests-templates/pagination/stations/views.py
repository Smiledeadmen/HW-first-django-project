import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    CONTENT = []
    with open(BUS_STATION_CSV, encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            CONTENT.append(row)
    paginator = Paginator(CONTENT, 10)
    current_page = int(request.GET.get('page', 1))
    pagi_data = paginator.get_page(current_page)
    page = {'has_previous': current_page - 1,
            'number': current_page,
            'has_next': current_page + 1,
            'previous_page_number': current_page - 1,
            'next_page_number': current_page + 1}
    return render(request, 'stations/index.html', context={
        'bus_stations': pagi_data,
        'current_page': current_page,
        'page': page,
    })

