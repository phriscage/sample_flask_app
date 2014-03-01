#from flask import Blueprint, request, render_template, redirect, url_for, \
    #abort, session, flash, g, jsonify
from flask import Blueprint, redirect, url_for, render_template, jsonify

core = Blueprint('core', __name__, template_folder='templates')

@core.route('/', methods=['GET'])
def get_index():
    """ root path redirect to login """
    return render_template('index.html', title='Home', 
        user={'nickname': 'Chris'})
    #return redirect(url_for('auth.login'))

#@core.route('/music', methods=['GET'])
#@login_required
#def get_music():
    #""" get the music page """
    #return render_template('core/music.html')
