import pytest
from pydantic import ValidationError
from app.schemas.customer import CustomerUpdate


def test_customer_update_valid_data():
    data = {"name": "John Doe", "email": "john.doe@example.com"}
    customer = CustomerUpdate(**data)
    assert customer.name == "John Doe"
    assert customer.email == "john.doe@example.com"


def test_customer_update_invalid_email():
    data = {"name": "John Doe", "email": "not-an-email"}
    with pytest.raises(ValidationError):
        CustomerUpdate(**data)


def test_customer_update_missing_name():
    data = {"email": "john.doe@example.com"}
    with pytest.raises(ValidationError):
        CustomerUpdate(**data)


def test_customer_update_missing_email():
    data = {"name": "John Doe"}
    with pytest.raises(ValidationError):
        CustomerUpdate(**data)