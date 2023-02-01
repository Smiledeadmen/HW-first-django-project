from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    if sort == 'name':
        phones_obj = Phone.objects.order_by(sort)
    elif sort == 'min_price':
        phones_obj = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones_obj = Phone.objects.order_by('-price')
    else:
        phones_obj = Phone.objects.all()
    context = {'phones': phones_obj}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
