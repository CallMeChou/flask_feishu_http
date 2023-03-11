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
        "function1":"报工查询",
        "function2": "其他",
        "function3": "待开发"
    })

@app.route('/报工查询')
def function1():
    from check import main
    name="小周"
    webhook="https://www.feishu.cn/flow/api/trigger-webhook/c902ef4c9b6a57988ef22516cec91cac"
    main(name,webhook)
    return 



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
