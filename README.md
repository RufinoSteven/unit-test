# Banca Web - Caso de Estudio

Este proyecto simula funcionalidades básicas de una banca web, permitiendo la creación de clientes y transferencias de fondos entre cuentas.

## Estructura
- `/src`: Código fuente principal
- `/tests`: Pruebas unitarias

## Funciones principales
### create_customer(name, gender, email)
- Crea un cliente nuevo.
- Valida que el nombre sea obligatorio y el email tenga formato válido.
- Retorna un diccionario con id, name, gender, email.

### fund_transfer(balance, amount, dest_account)
- Realiza una transferencia de fondos.
- Valida saldo suficiente y cuenta destino válida.
- Retorna el nuevo balance.

## Pruebas
Las pruebas unitarias están en `/tests/test_banking.py` y cubren:
- Creación de cliente: válida, falta de nombre, email inválido.
- Transferencia: válida, saldo insuficiente, cuenta destino inválida.

## Instalación y ejecución
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta pruebas:
   ```bash
   pytest
   ```
