from decimal import Decimal

from order import Order


class TestGetPrice:

    def test_calculate_price_with_given_discount(self, mocker):
        discount = Decimal('0.6')
        shipping_price = Decimal('10.15')
        product_price = Decimal('200.80')
        mocker.patch(
            'order.Product.get_price',
            return_value=product_price,
        )
        mocker.patch(
            'order.Customer.calculate_shipping_price',
            return_value=shipping_price,
        )

        expected_price = (shipping_price + product_price) * discount

        result = Order('0.6').get_order_price()

        assert result == expected_price

    def test_when_apis_are_down_order_price_is_zero(self, mocker):
        discount = Decimal('0.6')
        shipping_price = Decimal('0')
        product_price = Decimal('0')
        mocker.patch(
            'order.Product.get_price',
            return_value=product_price,
        )
        mocker.patch(
            'order.Customer.calculate_shipping_price',
            return_value=shipping_price,
        )

        expected_price = Decimal('0')

        result = Order(discount).get_order_price()

        assert result == expected_price
