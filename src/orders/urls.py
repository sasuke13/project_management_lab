from django.urls import path

from orders.views import OrdersListView, CreateOrderView, SentOrdersListView

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders_list_view'),
    path('create/', CreateOrderView.as_view(), name='orders_list_view'),
    path('state/sent/', SentOrdersListView.as_view(), name='orders_list_view'),
]
