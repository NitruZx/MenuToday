from flask import Blueprint, render_template, request, redirect, url_for
from MenuToday2 import *
views = Blueprint(__name__, "views")

@views.route('/', methods=["POST", "GET"])
def index():
    """home page"""
    ans = ''
    if request.method == "POST" and "fweight" in request.form and "fhight" in request.form:
        weight = float(request.form.get('weight'))
        hight = float(request.form.get('hight'))
        ans = bmi(weight, hight)
    return render_template("index.html", bmi=ans)
