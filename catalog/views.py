from django.shortcuts import render
from django.urls import reverse_lazy
from catalog.models import Product, Category, BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class HomeListView(ListView):
    model = Category
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная'
    }


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'
    extra_context = {
        'title': 'Категории'
    }


class ProductsInCategoryListView(ListView):
    model = Product
    template_name = 'catalog/products_in_category.html'
    extra_context = {
        'title': 'Товары категории'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    extra_context = {
        'title': 'Наши товары'
    }


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


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:list')
    extra_context = {
        'title': 'Ваш пост'
    }


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:list')
    extra_context = {
        'title': 'Ваш пост'
    }


class BlogPostListView(ListView):
    model = BlogPost
    extra_context = {
        'title': 'Посты'
    }


class BlogPostDetailView(DetailView):
    model = BlogPost
    extra_context = {
        'title': 'Ваш пост'
    }


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:list')
    extra_context = {
        'title': 'Удалить пост'
    }
