from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('customer_add.html')

@app.route('/submit', methods=['POST'])
def handle_form_submission():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    # Simple validation
    if not all([name, email, phone, address]):
        return jsonify({'error': 'Please fill out all fields.'}), 400

    # Here you can add code to save the data to a database or perform other actions

    return jsonify({'message': 'Customer added successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)