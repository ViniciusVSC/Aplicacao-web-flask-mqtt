from flask import Blueprint, render_template
from models.iot.leitura import Leitura

ligar_bp = Blueprint('ligar', __name__,template_folder='./views/')

@ligar_bp.route('/ligar')
def ligar():
    return render_template('ligar.html')


