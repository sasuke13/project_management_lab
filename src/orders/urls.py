from django.urls import path

from orders.views import OrdersListView

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders_list_view')
]
