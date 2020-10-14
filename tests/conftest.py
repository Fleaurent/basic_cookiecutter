"""
conftest.py - global fixtures
"""
import pytest


@pytest.fixture
def global_user():
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
