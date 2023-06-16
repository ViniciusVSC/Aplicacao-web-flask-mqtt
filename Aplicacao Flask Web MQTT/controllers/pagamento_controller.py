from flask import Blueprint, render_template

pagamento_bp = Blueprint('pagamento', __name__,template_folder='./templates/')

@pagamento_bp.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')
