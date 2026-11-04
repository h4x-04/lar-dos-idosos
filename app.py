from flask import Flask, render_template, request, redirect, url_for, flash
import banco

app = Flask(__name__)
app.secret_key = "uninter_extensao_lar_wb_secret"

# Garante que o banco de dados SQL e as tabelas estejam criados
banco.inicializar_banco()

@app.route("/")
def index():
    """Página principal do portal institucional."""
    return render_template("index.html")

@app.route("/doar", methods=["POST"])
def registrar_doacao():
    """Recebe dados do formulário e grava no banco de dados via SQL."""
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    tipo = request.form.get("tipo")
    descricao = request.form.get("descricao")
    horario = request.form.get("horario")

    if nome and telefone and tipo and descricao:
        banco.cadastrar_doacao(nome, telefone, tipo, descricao, horario)
        flash("Sua intenção de doação foi registrada com sucesso! A equipe do Lar agradece seu carinho. ❤️", "sucesso")
    else:
        flash("Por favor, preencha todos os campos obrigatórios.", "erro")

    return redirect(url_for("index") + "#formulario-doacao")

@app.route("/admin")
def painel_admin():
    """Painel administrativo para a equipe do asilo gerenciar as doações registradas."""
    doacoes = banco.listar_doacoes()
    totais = banco.obter_totais()
    return render_template("admin.html", doacoes=doacoes, totais=totais)

@app.route("/admin/status/<int:doacao_id>/<string:novo_status>")
def atualizar_status(doacao_id, novo_status):
    """Atualiza se a doação já foi recebida pela recepção."""
    banco.alterar_status_doacao(doacao_id, novo_status)
    return redirect(url_for("painel_admin"))

@app.route("/admin/excluir/<int:doacao_id>")
def excluir_doacao(doacao_id):
    """Exclui uma doação do banco de dados via SQL DELETE."""
    banco.excluir_doacao(doacao_id)
    return redirect(url_for("painel_admin"))

if __name__ == "__main__":
    print("Iniciando Portal Lar dos Idosos WB...")
    print("Acesse no navegador: http://127.0.0.1:5000")
    print("Painel administrativo: http://127.0.0.1:5000/admin")
    app.run(debug=True, port=5000)
