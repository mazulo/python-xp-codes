from decimal import Decimal

import requests


PRICING_API_URL = 'http://127.0.0.1:8000/pricing/'


class Product:

    def get_price(self):
        params = {
            'product': 'celular',
        }
        response = requests.get(PRICING_API_URL, params=params)
        result = response.json()
        return Decimal(result.get('price'))
