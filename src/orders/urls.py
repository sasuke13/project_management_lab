from django.urls import path

from orders.views import OrdersListView, CreateOrderView

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders_list_view'),
    path('create/', CreateOrderView.as_view(), name='orders_list_view'),
]
