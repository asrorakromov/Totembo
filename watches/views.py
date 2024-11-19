from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView

from watches.models import Product, Categories


class ProductListView(ListView):
    model = Product
    context_object_name = 'categories'
    template_name = 'watches/index.html'
    extra_context = {
        'title': 'ТОТЕМВО'
    }

    def get_queryset(self):
        categories = Categories.objects.all()
        return categories
