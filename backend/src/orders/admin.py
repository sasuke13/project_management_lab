from django.contrib import admin

from orders.models import Orders, States


class StatesModelAdmin(admin.ModelAdmin):
    fields = ['states']


admin.site.register(Orders)
admin.site.register(States, StatesModelAdmin)
