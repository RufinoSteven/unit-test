
from flask import Flask, request, jsonify, render_template_string
from banking import create_customer, fund_transfer

app = Flask(__name__)

# Plantilla HTML con CSS
HTML = '''
<html>
<head>
<style>
body {
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    margin: 0;
    padding: 0;
}
.container {
    max-width: 500px;
    margin: 40px auto;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    padding: 32px 24px;
}
h2 {
    color: #2c3e50;
    margin-top: 0;
}
form {
    margin-bottom: 24px;
}
label {
    display: block;
    margin-bottom: 6px;
    font-weight: bold;
}
input[type="text"], input[type="number"], input[type="email"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}
input[type="submit"] {
    background: #2980b9;
    color: #fff;
    border: none;
    padding: 10px 18px;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.2s;
}
input[type="submit"]:hover {
    background: #1c5980;
}
.result {
    background: #eafaf1;
    border-left: 4px solid #27ae60;
    padding: 12px;
    margin-top: 16px;
    font-size: 16px;
    color: #2c3e50;
}
.error {
    background: #ffeaea;
    border-left: 4px solid #e74c3c;
    padding: 12px;
    margin-top: 16px;
    font-size: 16px;
    color: #2c3e50;
}
</style>
</head>
<body>
<div class="container">
<h2>Crear Cliente</h2>
<form method="post" action="/customer_view">
    <label>Nombre:</label>
    <input name="name" type="text" required>
    <label>Género:</label>
    <input name="gender" type="text">
    <label>Email:</label>
    <input name="email" type="email" required>
    <input type="submit" value="Crear Cliente">
</form>
<hr>
<h2>Transferencia de Fondos</h2>
<form method="post" action="/transfer_view">
    <label>Saldo:</label>
    <input name="balance" type="number" required>
    <label>Monto:</label>
    <input name="amount" type="number" required>
    <label>Cuenta destino:</label>
    <input name="dest_account" type="text" required>
    <input type="submit" value="Transferir">
</form>
<hr>
{% if result %}
    {% if 'Error:' in result %}
        <div class="error">{{ result|safe }}</div>
    {% else %}
        <div class="result">{{ result|safe }}</div>
    {% endif %}
{% endif %}
</div>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML, result="")

@app.route('/customer_view', methods=['POST'])
def customer_view():
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')
    try:
        customer = create_customer(name, gender, email)
        result = f"<b>Cliente creado:</b> {customer}"
    except Exception as e:
        result = f"<b>Error:</b> {str(e)}"
    return render_template_string(HTML, result=result)

@app.route('/transfer_view', methods=['POST'])
def transfer_view():
    balance = request.form.get('balance')
    amount = request.form.get('amount')
    dest_account = request.form.get('dest_account')
    try:
        new_balance = fund_transfer(float(balance), float(amount), dest_account)
        result = f"<b>Transferencia exitosa. Nuevo saldo:</b> {new_balance}"
    except Exception as e:
        result = f"<b>Error:</b> {str(e)}"
    return render_template_string(HTML, result=result)

# Endpoints API JSON
@app.route('/customer', methods=['POST'])
def customer():
    data = request.get_json()
    try:
        customer = create_customer(data['name'], data.get('gender', ''), data['email'])
        return jsonify(customer), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.get_json()
    try:
        new_balance = fund_transfer(data['balance'], data['amount'], data['dest_account'])
        return jsonify({'new_balance': new_balance}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
