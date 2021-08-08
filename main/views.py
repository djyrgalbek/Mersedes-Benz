from datetime import timedelta, datetime

from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .forms import ProductForm, CreateProductForm, UpdateProductForm
from .models import *


from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Представление для index.html
class MainPageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 3


# Представление для search.html
class SearchPageView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        context['products'] = Product.objects.filter(Q(name__icontains=search) |
                                                    Q(price__icontains=search) |
                                                    Q(year_of_issue__icontains=search) |
                                                     Q(engine__icontains=search) |
                                                     Q(transmission__icontains=search) |
                                                     Q(steering_wheel__icontains=search) |
                                                     Q(steering_wheel__icontains=search) |
                                                     Q(color__icontains=search))
        context['search'] = search
        return context


# Представление для filter-product.html
class FilterPageView(ListView):
    model = Product
    template_name = 'filter-product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = self.request.GET.get('filter')

        if filter == "new":
            start_date = timezone.now() - timedelta(days=1)
            context['products'] = Product.objects.filter(created__gte=start_date)
            context['category'] = 'Новые'
        elif filter == "cheap":
            context['products'] = Product.objects.filter(price__lte=350000)
            context['category'] = 'Дешевые'
        elif filter == "expensive":
            context['products'] = Product.objects.filter(price__gte=350001)
            context['category'] = 'Дорогие'
        else:
            context['products'] = Product.objects.all()
        return context


# Представление для category-detail.html
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category_id=self.slug)
        print(self.slug)
        return context


# Представление для product-detail.html
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_discount'] = Product.objects.filter().exclude(discount=0)
        return context


# Mixin для проверки аутентификации пользователя
class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


# Представление для add-product.html
class ProductCreateView(IsAdminCheckMixin, CreateView):
    model = Product
    template_name = 'add-product.html'
    form_class = CreateProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


# Представление для update-product.html
class ProductUpdateView(IsAdminCheckMixin, UpdateView):
    model = Product
    template_name = 'update-product.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


# Представление для delete-product.html
class DeleteProductView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'delete-product.html'
    success_url = reverse_lazy('home')
    context_object_name = 'product'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Продукт успешно удален!')
        return HttpResponseRedirect(success_url)



# Представления cart
@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')