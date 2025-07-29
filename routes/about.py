from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response, flash
#from app import DAO
from Misc.functions import *

about_view = Blueprint('about_routes', __name__, template_folder='/templates')

@about_view.route('/about', methods=["GET"])
def home():
    return render_template('about.html')