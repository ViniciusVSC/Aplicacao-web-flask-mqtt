from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.iot.leitura import Leitura
from models.db import db

listar_menssagem_bp = Blueprint('listar_menssagem', __name__, template_folder='./views')

@listar_menssagem_bp.route("/list_reads")
def listar_menssagem():
    leituras = Leitura.select_leituras()
    return render_template("list_reads.html", leituras=leituras)