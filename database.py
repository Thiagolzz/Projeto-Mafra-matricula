
import sqlite3


def conectar():
    conexao = sqlite3.connect("matriculas.db")

    # Faz o SQLite retornar os resultados como dicionários.
    conexao.row_factory = sqlite3.Row

    return conexao


def inicializar_database():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota REAL NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()
