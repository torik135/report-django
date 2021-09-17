from django.shortcuts import render
import pandas as pd
# from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm
from .utils import get_salesman_from_id, get_customer_from_id

def home_view(request):
    sales_df = None
    positions_df = None

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

            # get name from the id
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(get_salesman_from_id)
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_customer_from_id)
            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime(('%Y-%m-%d')))
            
            # change the column name
            sales_df.rename({
                'salesman_id': 'salesman',
                'customer_id': 'customer',
                }, 
                axis=1,
                inplace=True)

            positions_data = []
            
            for sale in queryset:
                for pos in sale.get_positions():
                    obj = {
                        'position_id':pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'sales_id': pos.get_sales_id(),
                    }

                    positions_data.append(obj)

            positions_df = pd.DataFrame(positions_data)
            # print('positions_df')
            # print(positions_df)

            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            # print(sales_df)
        else: print('query err!')

    context = {
        'title': title,
        'form': form,
        'sales_df': sales_df,
        'positions_df': positions_df,
    }
    return render(request, 'sales/home.html', context=context)

# Class-based view
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