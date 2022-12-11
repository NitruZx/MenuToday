from flask import Blueprint, render_template, request, redirect, url_for
from MenuToday2 import *
views = Blueprint(__name__, "views")

@views.route('/', methods=["POST", "GET"])
def index():
    """home page"""
    if request.method == "GET":
        tmp = ["", "", ""]
        return render_template("index.html", tmp = tmp)
    if request.method == "POST":
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        age = int(request.form.get('age'))
        sex = request.form.get('sex')
        tmp = [weight, height, age]
        bmi_out = "%.2f"%bmi(weight, height)
        bmr_out = bmr(weight, height, age, sex)
    return render_template("index.html", bmi_out = bmi_out, bmr_out = bmr_out, tmp = tmp)
