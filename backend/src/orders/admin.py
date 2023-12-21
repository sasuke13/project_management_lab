from django.contrib import admin

from orders.models import Orders, States

admin.site.register(Orders)
admin.site.register(States)
