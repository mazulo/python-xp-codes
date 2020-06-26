from decimal import Decimal

import requests

SHIPPING_API_URL = 'http://127.0.0.1:8000/shipping/'


class Customer:

    def calculate_shipping_price(self):
        shipping_from = '64215-415'
        shipping_to = '22210-050'
        params = {
            'from': shipping_from,
            'to': shipping_to,
        }
        response = requests.get(SHIPPING_API_URL, params=params)

        if response.status_code == 200:
            result = response.json()
            price = Decimal(result.get('price'))
        else:
            price = Decimal('0')

        return price
