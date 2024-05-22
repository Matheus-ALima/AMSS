from flask import Blueprint, render_template

#iniciando o blueprint
menu_route = Blueprint('menu', __name__)

#definindo rotas do menu
@menu_route.route('/')
def menu():
    return render_template('menu.html')
