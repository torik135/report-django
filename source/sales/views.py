from django.shortcuts import render
# from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm

def home_view(request):
    form = SaleSearchForm(request.POST or None)
    title = 'home'
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'sales/home.html', context=context)

# Class-nased view
# class SaleListView(ListView):
#     model = Sale
#     template_name = "sales/main.html"
#     context_object_name = "data"
# class SaleDetailView(DetailView):
#     model = Sale
#     template_name = "sales/detail.html"

def sale_list_view(request):
    queryset = Sale.objects.all()
    return render(request, 'sales/main.html', {'data': queryset}) 

def sale_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk=pk)
    return render(request, 'sales/detail.html', {'object': obj}) 