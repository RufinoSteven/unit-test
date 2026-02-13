import pytest
from src.banking import create_customer, fund_transfer

# Pruebas para create_customer

def test_create_customer_valid():
    customer = create_customer("Juan", "M", "juan@email.com")
    assert customer["name"] == "Juan"
    assert customer["gender"] == "M"
    assert customer["email"] == "juan@email.com"
    assert "id" in customer


def test_create_customer_missing_name():
    with pytest.raises(ValueError) as exc:
        create_customer("", "F", "ana@email.com")
    assert "obligatorio" in str(exc.value)


def test_create_customer_invalid_email():
    with pytest.raises(ValueError) as exc:
        create_customer("Ana", "F", "anaemail.com")
    assert "inválido" in str(exc.value)

# Pruebas para fund_transfer

def test_fund_transfer_valid():
    new_balance = fund_transfer(1000, 200, "ACC123")
    assert new_balance == 800


def test_fund_transfer_insufficient_balance():
    with pytest.raises(ValueError) as exc:
        fund_transfer(100, 200, "ACC123")
    assert "insuficiente" in str(exc.value)


def test_fund_transfer_invalid_dest_account():
    with pytest.raises(ValueError) as exc:
        fund_transfer(500, 100, "")
    assert "inválida" in str(exc.value)
