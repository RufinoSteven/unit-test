import re
import uuid

# Validación de email usando regex simple
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def create_customer(name, gender, email):
    """
    Crea un cliente nuevo.
    Args:
        name (str): Nombre del cliente (obligatorio)
        gender (str): Género del cliente
        email (str): Email del cliente (debe ser válido)
    Returns:
        dict: Cliente con id, name, gender, email
    Raises:
        ValueError: Si falta el nombre o el email es inválido
    """
    if not name or not name.strip():
        raise ValueError("El nombre es obligatorio.")
    if not re.match(EMAIL_REGEX, email):
        raise ValueError("Email inválido.")
    customer_id = str(uuid.uuid4())
    return {
        "id": customer_id,
        "name": name,
        "gender": gender,
        "email": email
    }


def fund_transfer(balance, amount, dest_account):
    """
    Realiza una transferencia de fondos.
    Args:
        balance (float): Saldo actual
        amount (float): Monto a transferir
        dest_account (str): Cuenta destino (debe ser válida)
    Returns:
        float: Nuevo saldo
    Raises:
        ValueError: Si el saldo es insuficiente o la cuenta destino es inválida
    """
    if amount > balance:
        raise ValueError("Saldo insuficiente.")
    if not dest_account or not dest_account.strip():
        raise ValueError("Cuenta destino inválida.")
    # Aquí se podría agregar lógica para validar el formato de la cuenta
    return balance - amount

# Comentarios explicativos incluidos en cada función para claridad.
