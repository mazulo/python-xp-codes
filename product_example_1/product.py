from decimal import Decimal
from time import sleep


class Product:

    def get_price(self):
        sleep(5)
        return Decimal('200.80')
