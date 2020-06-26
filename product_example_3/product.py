from decimal import Decimal

import requests


PRICING_API_URL = 'http://127.0.0.1:8000/pricing/'


class Product:

    def get_price(self):
        params = {
            'product': 'celular',
        }
        response = requests.get(PRICING_API_URL, params=params)
        if response.status_code == 200:
            result = response.json()
            price = Decimal(result.get('price'))
        else:
            price = Decimal('0')

        return price
