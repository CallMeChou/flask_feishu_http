from flask import Flask, jsonify
import os
from functions import sheet_read

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def root():
    return '（手动狗头）🈲❌❗⚠'

@app.route('/function')
def bot_test():
    return jsonify({
        "info":"发送对应功能即可",
        "function1":"功能列表",
        "function2": "报工情况查询",
        "function3": "待开发"
    })

@app.route('/function1')
def function1():




if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
