from django.shortcuts import render
import pandas as pd
# from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm

def home_view(request):
    sales_df = None

    form = SaleSearchForm(request.POST or None)
    title = 'home'

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        # get all object from Sale
        queryset = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(queryset) > 0:
            sales_df = pd.DataFrame(queryset.values())

            sales_df = sales_df.to_html()
            print(sales_df)
        else: print('query err!')

    context = {
        'title': title,
        'form': form,
        'sales_df': sales_df,
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