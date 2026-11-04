import sqlite3
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(DIRETORIO_ATUAL, "doacoes.db")
SCHEMA_PATH = os.path.join(DIRETORIO_ATUAL, "schema.sql")

def obter_conexao():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect(DATABASE_PATH)
    # Permite acessar colunas por nome como dicionário (ex: linha['nome_doador'])
    conexao.row_factory = sqlite3.Row
    return conexao

def inicializar_banco():
    """Executa o script SQL para criar as tabelas se ainda não existirem."""
    if not os.path.exists(DATABASE_PATH):
        conexao = obter_conexao()
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            script_sql = f.read()
        conexao.executescript(script_sql)
        conexao.commit()
        conexao.close()
        print("Banco de dados 'doacoes.db' inicializado com sucesso!")
    else:
        print("Banco de dados 'doacoes.db' já existente e pronto.")

def cadastrar_doacao(nome, telefone, tipo, descricao, horario):
    """Insere um novo registro de doação utilizando comando SQL INSERT."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    sql = """
        INSERT INTO doacoes (nome_doador, telefone, tipo_doacao, descricao_itens, horario_preferencial, status)
        VALUES (?, ?, ?, ?, ?, 'Pendente')
    """
    cursor.execute(sql, (nome, telefone, tipo, descricao, horario))
    conexao.commit()
    conexao.close()

def listar_doacoes():
    """Consulta todas as doações registradas usando comando SQL SELECT."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    sql = "SELECT * FROM doacoes ORDER BY id DESC"
    cursor.execute(sql)
    doacoes = cursor.fetchall()
    conexao.close()
    return doacoes

def alterar_status_doacao(doacao_id, novo_status):
    """Atualiza o status de uma doação usando comando SQL UPDATE."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    sql = "UPDATE doacoes SET status = ? WHERE id = ?"
    cursor.execute(sql, (novo_status, doacao_id))
    conexao.commit()
    conexao.close()

def excluir_doacao(doacao_id):
    """Exclui um registro de doação usando comando SQL DELETE."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    sql = "DELETE FROM doacoes WHERE id = ?"
    cursor.execute(sql, (doacao_id,))
    conexao.commit()
    conexao.close()

def obter_totais():
    """Calcula estatísticas de doações para o painel administrativo usando SQL."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) AS total FROM doacoes")
    total = cursor.fetchone()['total']
    cursor.execute("SELECT COUNT(*) AS pendentes FROM doacoes WHERE status = 'Pendente'")
    pendentes = cursor.fetchone()['pendentes']
    cursor.execute("SELECT COUNT(*) AS recebidas FROM doacoes WHERE status = 'Recebido'")
    recebidas = cursor.fetchone()['recebidas']
    conexao.close()
    return {"total": total, "pendentes": pendentes, "recebidas": recebidas}

if __name__ == "__main__":
    inicializar_banco()
    print("Totais atuais no SQL:", obter_totais())
