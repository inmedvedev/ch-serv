from django.core.management import BaseCommand, CommandError
from django.conf import settings
from gsheets.models import Order
from datetime import date, timedelta
import telegram


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
           main()
        except Exception as exc:
            raise CommandError(exc)


def main():
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    date_yesterday = date.today() - timedelta(days=1)
    for order in Order.objects.filter(delivery_time=date_yesterday):
        try:
            bot.send_message(
                text=f'Срок поставки заказа №{order.number} прошел!',
                chat_id=settings.TELEGRAM_CHAT_ID
            )
        except Exception as err:
            print(err)
        order.notification_sent = True
        order.save()
