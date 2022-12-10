from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, "views")

@views.route('/')
def index():
    """home page"""
    weight = request.form["fweight"]
    return render_template("index.html")
