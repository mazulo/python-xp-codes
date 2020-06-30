import re
import json
from decimal import Decimal

import httpretty
import pytest

from order import Order


@pytest.fixture
def shipping_price():
    price = Decimal('10.15')

    return price


@pytest.fixture
def product_price():
    price = Decimal('200.80')

    return price


def response_factory(status_code, body_dict={}):
    def request_callback(request, uri, response_headers):
        return [status_code, response_headers, json.dumps(body_dict)]

    return request_callback


class TestGetPrice:

    @httpretty.activate
    def test_calculate_price_with_given_discount(
        self,
        shipping_price,
        product_price,
    ):
        discount = Decimal('0.6')

        uri = re.compile(r'http://127.0.0.1:8000/*')
        shipping_body = {"price": str(shipping_price)}
        product_body = {"price": str(product_price)}
        httpretty.register_uri(
            httpretty.GET,
            uri,
            body=response_factory(200, shipping_body),
        )
        httpretty.register_uri(
            httpretty.GET,
            uri,
            body=response_factory(200, product_body),
        )

        expected_price = (shipping_price + product_price) * discount

        result = Order(discount).get_order_price()

        assert result == expected_price

    @httpretty.activate
    def test_when_apis_are_down_order_price_is_zero(
        self,
        shipping_price,
        product_price,
    ):
        discount = Decimal('0.6')
        uri = re.compile(r'http://127.0.0.1:8000/*')
        httpretty.register_uri(
            httpretty.GET,
            uri,
            body=response_factory(403),
        )
        httpretty.register_uri(
            httpretty.GET,
            uri,
            body=response_factory(403),
        )

        expected_price = Decimal('0')

        result = Order(discount).get_order_price()

        assert result == expected_price
