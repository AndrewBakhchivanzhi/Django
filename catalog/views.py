from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
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

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('name', 'description',)
    extra_context = {
        'title': 'Ваш пост'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class BlogPostListView(ListView):
    model = BlogPost
    extra_context = {
        'title': 'Посты'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset



class BlogPostDetailView(DetailView):
    model = BlogPost
    extra_context = {
        'title': 'Ваш пост'
    }


    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:list')
    extra_context = {
        'title': 'Удалить пост'
    }
