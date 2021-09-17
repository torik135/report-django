from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Sale

def home_view(request):
    title = 'home'
    return render(request, 'sales/home.html', {'title': title})

class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html"
    context_object_name = "data"
class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"
