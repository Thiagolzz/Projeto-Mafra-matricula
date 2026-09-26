from time import sleep

alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira  nota: "))
    nota2 = float(input("Digite a segunda  nota: "))

    aluno = {
        "nome": nome,
        "notas": [nota1, nota2]
    }

    alunos.append(aluno)
    print(f"\nAluno {nome} adicionado com sucesso!")


def listar_alunos():
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado")
        return

    print("\n///// LISTA DE ALUNOS /////")

    for aluno in alunos:
        media = sum(aluno["notas"]) / len(aluno["notas"])

        print(f"Nome: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {media:.2f}")

def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que procura: ")

    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            media = sum(aluno["notas"]) / len(aluno["notas"])
            
            print(f"Nome: {aluno['nome']}")
            print(f"Notas: {aluno['notas']}")
            print(f"Média: {media:.2f}")

            encontrado = True
            break

    if not encontrado:
        print("\nAluno não encontrado.")

def remover_aluno():
    nome_remover = input("Digite o nome do aluno que deseja remover: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome_remover.lower():
            alunos.remove(aluno)
            print(f"\nAluno {nome_remover} removido com sucesso")
            return

def media_geral():
    if len(alunos) == 0:
        print("\nNenhum aluno encontrado")
        return

    todas_as_notas = []
    for aluno in alunos:
        todas_as_notas.extend(aluno["notas"])

        media = sum(todas_as_notas) / len(todas_as_notas)
        print(f"\nMédia de todos os alunos: {media:.2f}")

while True:
    print("\n----- MENU -----")

    print("1.Adicionar aluno")
    print("2.Listar todos os alunos")
    print("3.Buscar aluno pelo nome")
    print("4.Remover aluno")
    print("5.Mostrar média geral das notas")
    print("6.Sair")
    print("----------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "4":
        remover_aluno()

    elif opcao == "5":
        media_geral()

    elif opcao == "6":
        print("\nPrograma encerrado")
        break

    else:
        print("\nSelecione uma opção válida!")
        sleep(2)