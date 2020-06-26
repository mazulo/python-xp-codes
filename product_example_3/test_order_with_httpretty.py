import re
import json
from decimal import Decimal

import httpretty

from order import Order


API_URL = 'http://127.0.0.1:8000/'


class TestGetPrice:

    @httpretty.activate
    def test_calculate_price_with_given_discount(self, mocker):
        discount = Decimal('0.6')
        shipping_price = Decimal('10.15')
        product_price = Decimal('200.80')

        uri = re.compile(r'(?s).*')
        shipping_body = json.dumps(
            {"price": str(Decimal(shipping_price))}
        )
        pricing_body = json.dumps(
            {"price": str(Decimal(product_price))}
        )
        httpretty.register_uri(
            httpretty.GET,
            uri,
            body=shipping_body,
        )
        httpretty.register_uri(
            httpretty.GET,
            uri,
            body=pricing_body,
        )

        expected_price = (shipping_price + product_price) * discount

        result = Order('0.6').get_order_price()

        assert result == expected_price

    @httpretty.activate
    def test_when_apis_are_down_order_price_is_zero(self, mocker):
        uri = re.compile(r'(?s).*')
        httpretty.register_uri(
            httpretty.GET,
            uri,
            status=403,
        )
        httpretty.register_uri(
            httpretty.GET,
            uri,
            status=403,
        )

        expected_price = Decimal('0')

        result = Order('0.6').get_order_price()

        assert result == expected_price
