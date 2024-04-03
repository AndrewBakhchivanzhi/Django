from django.urls import path


from catalog.views import index, contacts, products

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/', products),
]
