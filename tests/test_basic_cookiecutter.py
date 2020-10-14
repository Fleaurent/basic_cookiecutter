#!/usr/bin/env python

"""
Tests for `basic_cookiecutter` package.
run test: pytest
run docstring test: pytest --doctest-modules
You can stop running tests after the first failure: pytest -x
Rerun only the failed tests from the previous run: pytest --lf
Start a debugger on failure: pytest --pdb

pytest-cov:
pytest --cov=myproj tests/
"""

import pytest


from basic_cookiecutter import basic_cookiecutter

# 1. fixtures
@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
    pass

@pytest.fixture
def user():
    """
    A fixture is a function that returns an object
    that can be used in the test
    """
    user = dict(
        first_name="Sebastian",
        last_name="Witowski",
        email="sebastian.witowski@example.com",
        role="customer",
    )
    return user


# 2. tests
def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert True


def test_add_two_numbers():
    """ simple test """
    assert 2+2 == 4


def test_checkout_process(user, global_user):
    """ test with local&global fixture"""
    print(user.keys())
    assert user["role"] == "customer"
    assert global_user["role"] == "customer"


# 3. parametrized test
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "number_of_orders,order_size",
    [
        (1, 1),
        (100, 1),
        (1, 100),
        (50, 50),
    ]
)
def test_placing_order(number_of_orders, order_size):
    """ paremeterized test """
    # order = place_order(number_of_orders, order_size)
    assert number_of_orders > 0
    assert order_size > 0


# 4. test documentation
# run pytest with --doctest-modules
def add_two_numbers(a, b):
    """ Adds two numbers
    >>> add_two_numbers(2, 2)
    5
    """
    return a + b
