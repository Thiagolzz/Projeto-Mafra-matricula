from time import sleep

# Lista onde serão armazenados todos os alunos cadastrados
alunos = []


def adicionar_aluno():
    # Pede o nome do aluno para fazer o cadastro
    nome = input("Digite o nome do aluno: ")

    # Validação da idade para evitar valores inválidos
    while True:
        try:
            idade = int(input("Digite a idade do aluno: "))

            if idade > 0:
                break

            print("A idade deve ser maior que zero.")

        except ValueError:
            print("Digite uma idade válida.")

    # A nota precisa ser um número entre 0 e 10
    while True:
        try:
            nota = float(input("Digite a nota do aluno (0 a 10): "))

            if 0 <= nota <= 10:
                break

            print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")

    # Dicionário com as informações do aluno
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    # Adiciona o aluno na lista principal
    alunos.append(aluno)

    print(f"\nAluno {nome} adicionado com sucesso!")


def listar_alunos():
    # Verifica se existe algum aluno cadastrado antes de listar
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.")
        return

    print("\n///// LISTA DE ALUNOS /////")

    # Percorre a lista e mostra os dados de cada aluno
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Nota: {aluno['nota']:.2f}")
        print("--------------------------")


def buscar_aluno():
    # Nome que será usado para procurar o aluno na lista
    nome_busca = input("Digite o nome do aluno que procura: ")

    # Começa como False e muda para True caso o aluno seja encontrado
    encontrado = False

    for aluno in alunos:
        # O lower() permite fazer a busca sem diferenciar maiúsculas e minúsculas
        if aluno["nome"].lower() == nome_busca.lower():
            print(f"\nNome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Nota: {aluno['nota']:.2f}")

            encontrado = True
            break

    # Se o nome não foi encontrado depois de percorrer a lista
    if not encontrado:
        print("\nAluno não encontrado.")


def remover_aluno():
    # Nome do aluno que será removido
    nome_remover = input("Digite o nome do aluno que deseja remover: ")

    # Variável usada para saber se o aluno foi encontrado
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_remover.lower():
            # Remove o aluno da lista
            alunos.remove(aluno)

            print(f"\nAluno {nome_remover} removido com sucesso.")

            encontrado = True
            break

    # Mostra uma mensagem caso nenhum aluno tenha o nome informado
    if not encontrado:
        print("\nAluno não encontrado.")


def media_geral():
    # Não é possível calcular a média se não houver alunos cadastrados
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.")
        return

    # Lista que vai armazenar somente as notas dos alunos
    todas_as_notas = []

    for aluno in alunos:
        todas_as_notas.append(aluno["nota"])

    # Soma todas as notas e divide pela quantidade de notas
    media = sum(todas_as_notas) / len(todas_as_notas)

    print(f"\nMédia geral das notas: {media:.2f}")


# O while mantém o programa funcionando até o usuário escolher sair
while True:
    print("\n----- MENU -----")

    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Remover aluno")
    print("5. Mostrar média geral das notas")
    print("6. Sair")

    print("----------------")

    opcao = input("Escolha uma opção: ")

    # Cada opção chama uma função diferente do sistema
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
        print("\nPrograma encerrado.")
        break

    else:
        # Caso o usuário digite uma opção que não existe no menu
        print("\nSelecione uma opção válida!")
        sleep(2)

