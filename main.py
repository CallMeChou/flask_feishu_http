from flask import Flask, jsonify,render_template,request
import os
from sql_connect import Mysql_con
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def root():
    return {"challenge": "test challenge"}

@app.route('/database_test')
def database_test():
    db=Mysql_con()
    results=db.get_data()
    return render_template("sql_select.html",results=results)

@app.route("/submit_insert")
def submit_insert():
    return render_template("sql_insert.html")
    

@app.route("/insert",methods=['GET','POST'])
def insert():
    if request.method == "POST":
        results = request.form
        db = Mysql_con()
        db.insertdata(results)
        return render_template("sql_insert.html",results=results)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
