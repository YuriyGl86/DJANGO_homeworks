from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort')
    sort_key = 'id'
    if sort_type == 'name':
        sort_key = 'name'
    elif sort_type == 'max_price':
        sort_key = '-price'
    elif sort_type == 'min_price':
        sort_key = 'price'

    phone_list = Phone.objects.all().order_by(sort_key)
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = list(Phone.objects.filter(slug=slug))[0]
    print(phone)
    context = {'phone': phone}
    return render(request, template, context)
