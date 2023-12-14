from django.contrib import admin

from orders.models import Orders, States


class StatesModelAdmin(admin.ModelAdmin):
    fields = ['states', 'changed_at']



admin.site.register(Orders)
admin.site.register(States, StatesModelAdmin)
