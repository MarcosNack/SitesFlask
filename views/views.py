
from main import app
from flask import render_template, request, flash, redirect, url_for


# Rotas
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        document = request.form.get("cpf_cnpj")
        if not document:
            flash("Por favor, insira um CPF ou CNPJ.", "error")
            return redirect(url_for("index"))  # Redireciona para a página para mostrar o alerta
        # Se o CPF/CNPJ for informado, você pode processar os dados aqui
        flash(f"Você inseriu o documento: {document}", "success")
        return redirect(url_for("index"))
    return render_template("index.html")


