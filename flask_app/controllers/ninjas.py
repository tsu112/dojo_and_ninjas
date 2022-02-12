from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models import dojo


@app.route('/ninjas')
def ninjas():
    return render_template('new_ninja.html', dojos=dojo.Dojo.get_all())


@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "age": request.form['age'],
        "dojos_id": request.form['dojos_id']
    }
    Ninja.create(data)
    return redirect('/')
