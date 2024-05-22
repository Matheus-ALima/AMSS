from flask import Flask
from routes.menu import menu_route

#inicialização
amss = Flask (__name__)

#aplicação
amss.register_blueprint(menu_route)

#execução
amss.run(debug=True)