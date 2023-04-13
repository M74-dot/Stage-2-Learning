import pytest
import math_func


def test_add():
    assert math_func.add(3,5) == 8
    assert math_func.add(10) == 12


def test_product():
    assert math_func.multiply(1) == 1
    assert math_func.multiply(10,10) == 100


# @pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello', ' World') 
    assert result == 'Hello World'
    assert 'Hello' in result
    assert 'sxnjc' not in result


@pytest.mark.parametrize('n1, n2, result',[
    (10,2,12),
    ('Manisha',' Mali','Manisha Mali')
])
def test_param_add(n1, n2, result):
    assert math_func.add(n1, n2) == result
