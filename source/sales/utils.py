import uuid
import base64
from customers.models import Customer
from profiles.models import Profiles
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns


def generate_code():
    code = str(uuid.uuid4()).replace('-', 'CODE')[:12]
    return code


def get_salesman_from_id(id):
    salesman = Profiles.objects.get(id=id)
    return salesman


def get_customer_from_id(id):
    customer = Customer.objects.get(id=id)
    return customer


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_key(res_by):
    if res_by == '#1':
        key = 'transaction_id'
    elif res_by == '#2':
        key = 'created'
    return key


def get_chart(chart_type, data, results_by, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))
    key = get_key(results_by)

    grouped_data = data.groupby(key, as_index=False)[
        'total_price'].agg('sum')

    if chart_type == '#1':
        print('bar chart')
        # plt.bar(data['transaction_id'], data['price'])
        sns.barplot(x=key, y='total_price', data=grouped_data)
    elif chart_type == '#2':
        print('pie chart')
        #labels = kwargs.get('labels')
        plt.pie(data=grouped_data, x='total_price',
                labels=grouped_data[key].values)
    elif chart_type == '#3':
        print('line chart')
        #plt.plot(grouped_data[key], grouped_data['total_price'])
        sns.lineplot(x=grouped_data[key], y='total_price', data=grouped_data)
    else:
        print('error: invalid chart type')

    # sizing the fig
    plt.tight_layout()
    chart = get_graph()
    return chart
