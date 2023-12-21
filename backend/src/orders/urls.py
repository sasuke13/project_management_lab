from django.urls import path

from orders.views import OrdersListView, CreateOrderView, SentOrdersListView, DeliveredOrdersListView, \
    UserOrdersListView

urlpatterns = [
    path('', UserOrdersListView.as_view(), name='user_orders_list_view'),
    path('statistic/', OrdersListView.as_view(), name='orders_list_view'),
    path('create/', CreateOrderView.as_view(), name='orders_list_view'),
    path('state/sent/', SentOrdersListView.as_view(), name='user_sent_orders_list_view'),
    path('state/delivered/', DeliveredOrdersListView.as_view(), name='user_delivered_orders_list_view'),
]
