from datetime import datetime, timedelta

from celery import shared_task
from django.db.models import Max

from orders.models import Orders


@shared_task
def cancel_inactive_orders():
    today_date = datetime.now().date()

    # Знаходимо останню дату зміни для кожного замовлення
    last_changed_dates = Orders.objects.annotate(
        last_change_date=Max('order_history__changed_at')
    )

    # Фільтруємо замовлення, які не мінялися протягом останніх 7 днів
    orders_not_changed_7_days = last_changed_dates.filter(
        last_change_date__lte=today_date - timedelta(days=7)
    )
    for order in orders_not_changed_7_days:
        order.order_history.states.append(order.state)
        order.state = 'CNL'
        order.save()
