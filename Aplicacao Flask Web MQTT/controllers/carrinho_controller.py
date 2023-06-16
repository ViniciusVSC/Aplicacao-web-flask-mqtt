from flask import Blueprint, render_template

carrinho_bp = Blueprint('carrinho', __name__,template_folder='./templates/')

@carrinho_bp.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')
