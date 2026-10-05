"""
Configure the flask application's pytest.
"""
import pytest
from app import app  

@pytest.fixture
def client():
    """
    Defines the pytest's client.
    """
    with app.test_client() as client:
        yield client
