from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/transactions', methods=['GET'])
def get_transactions():
    pass

@app.route('/home')
def home():
    return "Welcome to the Banking Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)