import pytest
from pydantic import ValidationError
from app.schemas.customer import CustomerUpdate


def test_customer_update_valid_name():
    data = {"name": "John Doe", "email": "john.doe@example.com"}
    customer = CustomerUpdate(**data)
    assert customer.name == "John Doe"


def test_customer_update_invalid_name():
    data = {"name": "", "email": "john.doe@example.com"}  # Invalid because name is empty
    with pytest.raises(ValidationError):
        CustomerUpdate(**data)


def test_customer_update_missing_name():
    data = {"email": "john.doe@example.com"}  # Invalid because name is missing
    with pytest.raises(ValidationError):
        CustomerUpdate(**data)