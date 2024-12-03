from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Random Number Generator! Visit /random to get a random number."

@app.route('/random')
def random_number():
    number = random.randint(1, 100) 
    return jsonify({"random_number": number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)