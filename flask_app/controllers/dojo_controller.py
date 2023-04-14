from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/dojos')
def dojo():
    dojos = Dojo.get_all()

    return render_template("index.html", dojos = dojos)



@app.route('/dojos/<int:id>')
def dojo_info(id):
    dojo_with_ninjas = Dojo.get_ninjas(id)
    return render_template("dojo_info.html", dojo = Dojo.get_one(id), ninjas = dojo_with_ninjas)

@app.route('/new_dojo', methods = ["POST"])
def create_dojo():
    Dojo.create(request.form)
    return redirect("/dojos")