
from database import conectar


def adicionar(nome, idade, nota):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)",
        (nome, idade, nota)
    )

    conexao.commit()
    conexao.close()


def listar():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    conexao.close()

    return alunos


def buscar(nome):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM alunos WHERE nome = ? COLLATE NOCASE",
        (nome,)
    )

    aluno = cursor.fetchone()

    conexao.close()

    return aluno


def remover(aluno_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM alunos WHERE id = ?",
        (aluno_id,)
    )

    conexao.commit()

    removido = cursor.rowcount > 0

    conexao.close()

    return removido


def media_geral():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT AVG(nota) FROM alunos")

    media = cursor.fetchone()[0]

    conexao.close()

    return media or 0
