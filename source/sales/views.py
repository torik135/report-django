from django.shortcuts import render
import pandas as pd
# from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm
from .utils import get_salesman_from_id, get_customer_from_id, get_chart
from reports.forms import ReportForm

def home_view(request):
    sales_df = None
    positions_df = None
    merged_df = None
    grouped_df = None
    chart = None

    search_form = SaleSearchForm(request.POST or None)
    report_form = ReportForm()
    
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
                'id': 'sales_id',
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
            # merge dataframe based on sales_id
            merged_df = pd.merge(sales_df, positions_df, on='sales_id')
            
            grouped_df = merged_df.groupby('transaction_id', as_index=False)['price'].agg('sum')

            chart = get_chart(chart_type, grouped_df, lables=grouped_df['transaction_id'].values)

            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()
            grouped_df = grouped_df.to_html()

            # print(sales_df)
        else: print('query err!')

    context = {
        'title': title,
        'search_form': search_form,
        'report_form': report_form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        'merged_df': merged_df,
        'grouped_df': grouped_df,
        'chart': chart,
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