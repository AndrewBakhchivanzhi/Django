from django.urls import path
from catalog.apps import MainConfig
from catalog.views import contacts, CategoryListView, \
    ProductListView, HomeListView, ProductsInCategoryListView, \
    BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/products_in_category/', ProductsInCategoryListView.as_view(), name='products_in_category'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('list/', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]
