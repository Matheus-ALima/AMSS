from flask import Blueprint, render_template
from database.usuario import USUARIO

#iniciando o blueprint
menu_route = Blueprint('menu', __name__)

#definindo rotas do menu
@menu_route.route('/')
def menu():
    return render_template('menu.html')

@menu_route.route('/')
def login():
    pass
    

@menu_route.route('/cadastrar')
def cadastrar():
    pass