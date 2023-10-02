from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    with open(BUS_STATION_CSV, encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        data = []
        for el in file_reader:
            data.append(el)
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(data, 10)
        page = paginator.get_page(page_number)
        context = {
            'page': page,
            }
        return render(request, 'stations/index.html', context)



