from flask import Flask, jsonify
import os
from functions import sheet_read

app = Flask(__name__)

@app.route('/feishu_test')
def root():
    return jsonify({"challenge": "11111","token": "yztvzXherBmpvy01Sje4Hf1RPa3HdkKu","type": "url_verification"})
    

@app.route('/table')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
