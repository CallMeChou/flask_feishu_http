from flask import Flask, jsonify
import os
from functions import sheet_read

app = Flask(__name__)
@app.route('/')
def root():
    return '（手动狗头）🈲❌❗⚠'

@app.route('/feishu_test')
def bot_test():
    return jsonify({"challenge": "11111","token": "yztvzXherBmpvy01Sje4Hf1RPa3HdkKu","type": "url_verification"})




if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
