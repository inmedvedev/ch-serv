from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from gsheets.models import Order
import gspread
from datetime import datetime
import requests
from xml.etree import ElementTree
from decimal import Decimal


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
           main()
        except Exception as exc:
            raise CommandError(exc)


def main():
    gc = gspread.service_account(filename='credetinals.json')
    sh = gc.open_by_url(settings.GOOGLE_SHEET_URL)
    worksheet = sh.get_worksheet(0)
    date_today = datetime.today().strftime('%d/%m/%Y')
    response = requests.get(f'https://www.cbr.ru/scripts/XML_daily_eng.asp?date_req={date_today}')
    tree = ElementTree.fromstring(response.content)
    doolar_rate = tree.find('.//Valute[@ID="R01235"]/Value').text.replace(',', '.')
    all_records = worksheet.get_all_records()
    orders = [
        Order(
            number=order['заказ №'],
            dollar_cost=round(Decimal(order['стоимость,$']), 2),
            ruble_cost=round(Decimal(order['стоимость,$'])*Decimal(doolar_rate), 2),
            delivery_time=datetime.strptime(order['срок поставки'], '%d.%m.%Y'),
        )
        for order in all_records
    ]
    Order.objects.all().delete()
    Order.objects.bulk_create(orders)
