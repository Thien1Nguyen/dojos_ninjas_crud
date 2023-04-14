from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all()

    return render_template("ninja.html", dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    print (request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")