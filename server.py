from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask JSON Server!"

@app.route('/data', methods=['GET'])
def get_data():
    data = {
        "name": "Aditya Suman",
        "age": 21,
        "city": "Patna"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
