from flask import render_template, redirect, request
from flask_app import app
# this imports the Dojo class in the model
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=dojos)


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.create(data)
    return redirect("/dojos")


@app.route('/dojo/<int:num>')
def read_one(num):
    data = {
        "id": num
    }
    this_dojo = Dojo.get_one(data)
    return render_template('dojos.html', dojo=Dojo.get_one(data))
