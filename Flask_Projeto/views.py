from main import app
from flask import render_template

# Rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/pedido")
def pedidos():
    return render_template("pedido.html")
