from decimal import Decimal

from product import Product
from customer import Customer


class Order:

    def __init__(self, discount=0.5):
        self.product = Product()
        self.customer = Customer()
        self.discount = Decimal(discount)

    def get_order_price(self):
        product_price = self.get_product_price()
        shipping_price = self.get_shipping_price()

        total = (product_price + shipping_price) * self.discount

        return total

    def get_product_price(self):
        return self.product.get_price()

    def get_shipping_price(self):
        return self.customer.calculate_shipping_price()
