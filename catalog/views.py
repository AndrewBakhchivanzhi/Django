from django.shortcuts import render
from catalog.models import Product, Category


def index(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def products_in_category(request, pk):
    category_items = Category.objects.get(pk=pk)
    product_list = Product.objects.filter(category_id=pk)
    context = {
        'object_list': product_list,
        'title': f'Товары категории {category_items.name}'
    }
    return render(request, 'catalog/products_in_category.html', context)


def products(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Наши товары'
    }
    return render(request, 'catalog/products.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html', context)



