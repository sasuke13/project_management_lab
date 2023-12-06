from datetime import datetime, timedelta

from celery import shared_task

from orders.models import Orders


@shared_task
def cancel_inactive_orders():
    today_date = datetime.now()

    orders = Orders.objects.filter(order_history__changed_at__range=[today_date - timedelta(days=7), today_date])

    for order in orders:
        order.order_history.states.append(order.state)
        order.state = 'CNL'

    orders.save()
