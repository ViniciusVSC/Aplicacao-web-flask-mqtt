from flask import Blueprint, render_template

produtos_bp = Blueprint('produtos', __name__,template_folder='./templates/')

@produtos_bp.route('/produtos')
def produtos():
    return render_template('produtos.html')
