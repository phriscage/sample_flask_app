from flask import Blueprint, redirect, url_for, render_template, jsonify

maps = Blueprint('maps', __name__, template_folder='templates')

@maps.route('', methods=['GET'])
def get_index():
    """ root path to index """
    return render_template('maps/index.html') 
