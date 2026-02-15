from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "Success", 
        "region": "Taiwan", 
        "auth_key": "Santhosh_Bypass_Active"
    })

if __name__ == "__main__":
    # Firebase Studio/IDX uses port 5000 by default
    app.run(host='0.0.0.0', port=5000)
