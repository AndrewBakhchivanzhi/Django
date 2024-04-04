from django.urls import path

from catalog.apps import MainConfig
from catalog.views import index, contacts, products, products_in_category

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('<int:pk>/products_in_category/', products_in_category, name='products_in_category')
]
