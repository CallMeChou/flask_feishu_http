from flask import Flask, jsonify
import os
from functions import sheet_read

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def root():
    return {"challenge": "test challenge"}


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
