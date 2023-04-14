import pytest


@pytest.fixture
def set_up():
    print('Browser opened')
    print('login')
    print('Browse product')
    yield
    print('logoff')
    print('Close browser')

def test_add_item_to_cart(set_up):
    print('Item added to the cart')


def test_remove_item_from_cart(set_up):
    print('Item removed from the cart')