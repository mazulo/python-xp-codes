from decimal import Decimal

from order import Order
from product import Product
from customer import Customer


class TestGetPrice:

    def test_calculate_price_with_given_discount(self):
        discount = Decimal('0.6')
        shipping_price = Customer().calculate_shipping_price()
        product_price = Product().get_price()

        expected_price = (shipping_price + product_price) * discount

        result = Order('0.6').get_order_price()

        assert result == expected_price
