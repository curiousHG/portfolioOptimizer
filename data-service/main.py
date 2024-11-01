# app.py
from flask import Flask, request, jsonify
import os
port = int(os.environ.get("PORT", 6000))

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def getData():
    

    
    return "Hello, World!"
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
