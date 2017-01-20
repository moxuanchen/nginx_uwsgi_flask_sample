# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template

api = Blueprint("api", __name__, static_folder="static", template_folder="templates")


@api.route('/')
def index():
    return render_template("index.html")

