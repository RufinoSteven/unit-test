
# Banca Web - Caso de Estudio

Este proyecto simula funcionalidades básicas de una banca web, permitiendo la creación de clientes y transferencias de fondos entre cuentas. Incluye pruebas unitarias, documentación y una API visual para pruebas.

## Estructura del Proyecto
- `/src`: Código fuente principal (`banking.py`, `app.py`)
- `/tests`: Pruebas unitarias (`test_banking.py`)
- `README.md`: Documentación
- `requirements.txt`: Dependencias
- `.gitignore`: Exclusión de archivos innecesarios

## Funcionalidades

### create_customer(name, gender, email)
Crea un cliente nuevo.
- Valida que el nombre sea obligatorio y el email tenga formato válido.
- Retorna un diccionario con id, name, gender, email.
- Lanza `ValueError` si los datos no son válidos.

### fund_transfer(balance, amount, dest_account)
Realiza una transferencia de fondos.
- Valida saldo suficiente y cuenta destino válida.
- Retorna el nuevo balance.
- Lanza `ValueError` si hay errores de validación.

## Pruebas Unitarias
Las pruebas están en `/tests/test_banking.py` y cubren:
- **create_customer:**
   - Creación válida
   - Falta de nombre
   - Email inválido
- **fund_transfer:**
   - Transferencia válida
   - Saldo insuficiente
   - Cuenta destino inválida

Cada prueba verifica caminos correctos y errores, usando `assert` y `pytest.raises`.

## API Visual (Flask)
Puedes probar la API visual ejecutando:

```bash
python src/app.py
```

### Endpoints
- **POST /customer**
   - Crea un cliente
   - Ejemplo JSON:
      ```json
      {
         "name": "Juan",
         "gender": "M",
         "email": "juan@email.com"
      }
      ```
- **POST /transfer**
   - Realiza una transferencia
   - Ejemplo JSON:
      ```json
      {
         "balance": 1000,
         "amount": 200,
         "dest_account": "ACC123"
      }
      ```

Puedes usar Postman, Insomnia o cURL para probar los endpoints.

## Instalación y Ejecución
1. Instala dependencias:
    ```bash
    python -m pip install -r requirements.txt
    ```
2. Ejecuta pruebas unitarias:
    ```bash
    python -m pytest
    ```
3. Inicia la API visual:
    ```bash
    python src/app.py
    ```

## Relación de pruebas con casos de uso
Las pruebas unitarias garantizan que:
- Se detectan errores de entrada (nombre/email/cuenta/saldo)
- Se valida la lógica de negocio
- Se cubren caminos correctos y errores

## Repositorio
El proyecto está versionado en GitHub:
https://github.com/RufinoSteven/unit-test.git

## Video de entrega
Se debe grabar un video mostrando:
- Estructura del proyecto
- Ejecución de pruebas unitarias
- Pruebas visuales de la API
- Explicación de la relación entre pruebas y casos de uso

---
Para dudas o mejoras, puedes modificar este README.
