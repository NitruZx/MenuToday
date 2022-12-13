from flask import Blueprint, render_template, request, redirect, url_for
from MenuToday4 import bmi, bmr, check_u_bmi, calpermeal, find_menu, outmenu
views = Blueprint(__name__, "views")

tmp = ["", "", "", ""]

@views.route('/', methods=["POST", "GET"])
def index():
    """home page"""
    if request.method == "GET":
        tmp = ["", "", "", ""]
        return render_template("index.html", tmp = tmp)
    if request.method == "POST":
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        age = int(request.form.get('age'))
        sex = request.form.get('sex')
        tmp = [weight, height, age, sex]
    return render_template("index.html", tmp = tmp) #bmi_out = bmi_out, bmr_out = bmr_out, tmp = tmp

@views.route('/bmi')
def calculate():
    """bmi cal page"""
    weight = float(request.args.get('weight'))
    height = float(request.args.get('height'))
    age = int(request.args.get('age'))
    sex = request.args.get('sex')
    bmi_out = "%.2f"%bmi(weight, height)
    bmr_out = bmr(weight, height, age, sex)
    body_out = check_u_bmi(bmi(weight, height))
    return render_template("random.html", bmi_out = bmi_out, bmr_out = bmr_out, tmp=["", "", ""], body_out = body_out)

@views.route('/meal', methods=["POST", "GET"])
def meal():
    """random meal page"""
    final = 0
    menu = ""
    if request.method == "GET":
        tmp = ["", "", ""]
        return render_template("random.html")
    if request.method == "POST":
        want1 = request.form.get('select1')
        want2 = request.form.get('select2')
        want3 = request.form.get('select3')
        if request.form.get('meal') is None:
            meal_day = 0
        else:
            meal_day = int(request.form.get('meal'))
        
        if request.form.get('cal') is None:
            cal_day = 0
        else:
            cal_day = int(request.form.get('cal'))
        
        try:
            menu = [i for i in [want1, want2, want3] if not i is None]
            final = outmenu(meal_day, menu, cal_day)
            tmp = [meal_day, cal_day, menu]
        except IndexError:
            final = ["", 0]
            return render_template("random.html", menu_out = final, tmp=["", "", ""])
    return render_template("random.html", menu_out = final, tmp=tmp)
