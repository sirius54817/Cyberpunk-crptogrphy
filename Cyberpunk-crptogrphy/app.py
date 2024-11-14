from flask import Flask, render_template, request, jsonify
import hashlib
import base64

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route for Hashing page
@app.route('/hash')
def hash_page():
    return render_template('hash.html')

# Route for Base64 page
@app.route('/base64')
def base64_page():
    return render_template('base64.html')

# Route for Cracking page
@app.route('/crack')
def crack_page():
    return render_template('crack.html')

# Hashing API endpoint
@app.route('/hash/calculate', methods=['POST'])
def hash_text():
    data = request.json
    text = data['text']
    algorithm = data['algorithm']
    result = calculate_hash(text, algorithm)
    return jsonify({'result': result})

# Base64 Encoding API endpoint
@app.route('/base64/encode', methods=['POST'])
def base64_encode():
    data = request.json
    text = data['text']
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return jsonify({'result': encoded})

# Base64 Decoding API endpoint
@app.route('/base64/decode', methods=['POST'])
def base64_decode():
    data = request.json
    encoded_text = data['encoded_text']
    try:
        decoded = base64.b64decode(encoded_text).decode('utf-8')
        return jsonify({'result': decoded})
    except Exception:
        return jsonify({'error': 'Invalid Base64 input'})

def calculate_hash(text, algorithm):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(text.encode('utf-8'))
    return hash_obj.hexdigest()

if __name__ == '__main__':
    app.run(debug=True)
