from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json(silent=True)
        
        if not data:
            return jsonify({'error': 'Invalid or missing JSON data'}), 400
        
        if 'num1' not in data or 'num2' not in data:
            return jsonify({'error': 'Both numbers are required'}), 400
        
        if 'operation' not in data:
            return jsonify({'error': 'Operation is required'}), 400
        
        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid number format'}), 400
        
        operation = data['operation']
        result = None
        error = None
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                error = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            error = "Invalid operation"
        
        if error:
            return jsonify({'error': error}), 400
        
        return jsonify({'result': result})
    
    except Exception:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
