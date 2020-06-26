from decimal import Decimal

from chalice import Chalice

app = Chalice(app_name='shipping-api')

MAP_FROM_TO_PRICES = {
    '64215-415:22210-050': Decimal('300'),
    '22210-050:64215-415': Decimal('350'),
}

MAP_PRODUCT_TO_PRICE = {
    'celular': Decimal('1000'),
    'notebook': Decimal('2000'),
}


@app.route('/shipping')
def shipping():
    request_dict = app.current_request.to_dict()
    query_params = request_dict.get('query_params')

    shipping_from = query_params.get('from')
    shipping_to = query_params.get('to')
    code = f'{shipping_from}:{shipping_to}'

    price = MAP_FROM_TO_PRICES.get(code)

    return {'price': str(Decimal(price))}


@app.route('/pricing')
def pricing():
    request_dict = app.current_request.to_dict()
    query_params = request_dict.get('query_params')

    product = query_params.get('product')

    price = MAP_PRODUCT_TO_PRICE.get(product)

    return {'price': str(Decimal(price))}
