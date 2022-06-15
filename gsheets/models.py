from django.db import models


class Order(models.Model):
    number = models.IntegerField('№ заказа')
    dollar_cost = models.DecimalField(
        'цена в долларах',
        max_digits=10,
        decimal_places=2
    )
    ruble_cost = models.DecimalField(
        'цена в рублях',
        max_digits=10,
        decimal_places=2
    )
    delivery_time = models.DateField('срок поставки')

    def __str__(self):
        return f'Номер заказа {self.number}'
