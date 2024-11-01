# app.py
from flask import Flask, request, jsonify
import os
port = int(os.environ.get("PORT", 6001))
print(port)


app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
     # data = request.json  # Expect JSON data in the POST request
    
    # if not data:
    #     return jsonify({"error": "No data provided"}), 400
    
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
