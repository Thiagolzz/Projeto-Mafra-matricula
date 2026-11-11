import customtkinter as ctk
from tkinter import ttk, messagebox

from aluno_service import adicionar, listar, buscar, remover, media_geral


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        # Configurações da janela.
        self.title("Sistema de Matrículas")
        self.geometry("1100x700")
        self.minsize(900, 600)

        # Define o tema escuro.
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configuração do layout principal.
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.criar_sidebar()
        self.criar_conteudo()

        # Carrega os alunos do banco ao abrir.
        self.atualizar_tabela()


    # Cria o menu lateral.
    def criar_sidebar(self):

        sidebar = ctk.CTkFrame(
            self,
            width=210,
            corner_radius=0
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        sidebar.grid_propagate(False)

        logo = ctk.CTkLabel(
            sidebar,
            text="MATRÍCULAS",
            font=("Arial", 22, "bold")
        )

        logo.pack(pady=35)

        menu = ctk.CTkLabel(
            sidebar,
            text="GERENCIAMENTO",
            text_color="gray",
            font=("Arial", 11)
        )

        menu.pack(padx=20, anchor="w")

        alunos_btn = ctk.CTkButton(
            sidebar,
            text="Alunos",
            command=self.atualizar_tabela
        )

        alunos_btn.pack(
            padx=15,
            pady=10,
            fill="x"
        )


    # Cria a área principal.
    def criar_conteudo(self):

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent"
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=25,
            pady=20
        )

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(2, weight=1)

        # Título.
        titulo = ctk.CTkLabel(
            self.content,
            text="Gerenciamento de Alunos",
            font=("Arial", 26, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 20)
        )

        # Formulário de cadastro.
        self.criar_formulario()

        # Área de listagem.
        self.criar_tabela()


    # Cria os campos de cadastro.
    def criar_formulario(self):

        form = ctk.CTkFrame(self.content)

        form.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(0, 20)
        )

        form.grid_columnconfigure((0, 1), weight=1)

        self.nome_input = ctk.CTkEntry(
            form,
            placeholder_text="Nome do aluno"
        )

        self.nome_input.grid(
            row=0,
            column=0,
            padx=15,
            pady=10,
            sticky="ew"
        )

        self.idade_input = ctk.CTkEntry(
            form,
            placeholder_text="Idade"
        )

        self.idade_input.grid(
            row=0,
            column=1,
            padx=15,
            pady=10,
            sticky="ew"
        )

        self.nota_input = ctk.CTkEntry(
            form,
            placeholder_text="Nota (0 a 10)"
        )

        self.nota_input.grid(
            row=1,
            column=0,
            padx=15,
            pady=10,
            sticky="ew"
        )

        cadastrar_btn = ctk.CTkButton(
            form,
            text="Adicionar aluno",
            command=self.adicionar_aluno
        )

        cadastrar_btn.grid(
            row=1,
            column=1,
            padx=15,
            pady=10,
            sticky="ew"
        )


    # Cria a tabela de alunos.
    def criar_tabela(self):

        container = ctk.CTkFrame(self.content)

        container.grid(
            row=2,
            column=0,
            sticky="nsew"
        )

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)

        # Campo de pesquisa.
        self.busca_input = ctk.CTkEntry(
            container,
            placeholder_text="Buscar aluno pelo nome..."
        )

        self.busca_input.grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="ew"
        )

        buscar_btn = ctk.CTkButton(
            container,
            text="Buscar",
            width=100,
            command=self.buscar_aluno
        )

        buscar_btn.grid(
            row=0,
            column=1,
            padx=10,
            pady=15
        )

        # Treeview é o componente de tabela do Tkinter.
        self.tabela = ttk.Treeview(
            container,
            columns=("id", "nome", "idade", "nota"),
            show="headings"
        )

        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("idade", text="Idade")
        self.tabela.heading("nota", text="Nota")

        self.tabela.column("id", width=50)
        self.tabela.column("nome", width=250)
        self.tabela.column("idade", width=100)
        self.tabela.column("nota", width=100)

        self.tabela.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=15,
            pady=10
        )

        # Botão de remoção.
        remover_btn = ctk.CTkButton(
            container,
            text="Remover selecionado",
            fg_color="#B91C1C",
            hover_color="#991B1B",
            command=self.remover_aluno
        )

        remover_btn.grid(
            row=2,
            column=0,
            padx=15,
            pady=15,
            sticky="w"
        )

        # Mostra a média geral.
        self.media_label = ctk.CTkLabel(
            container,
            text="Média geral: 0.00",
            font=("Arial", 16, "bold")
        )

        self.media_label.grid(
            row=2,
            column=1,
            padx=15,
            pady=15,
            sticky="e"
        )


    # Cadastra um novo aluno.
    def adicionar_aluno(self):

        nome = self.nome_input.get().strip()
        idade = self.idade_input.get().strip()
        nota = self.nota_input.get().strip().replace(",", ".")

        # Validação do nome.
        if not nome:
            messagebox.showwarning(
                "Atenção",
                "Informe o nome do aluno."
            )
            return

        # Validação da idade.
        try:
            idade = int(idade)

            if idade <= 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Atenção",
                "Informe uma idade válida."
            )
            return

        # Validação da nota.
        try:
            nota = float(nota)

            if not 0 <= nota <= 10:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Atenção",
                "A nota deve estar entre 0 e 10."
            )
            return

        try:
            # Chama o Service para salvar no database
            adicionar(nome, idade, nota)

            messagebox.showinfo(
                "Sucesso",
                f"Aluno {nome} cadastrado!"
            )

            # Limpa os campos.
            self.nome_input.delete(0, "end")
            self.idade_input.delete(0, "end")
            self.nota_input.delete(0, "end")

            # Atualiza a tabela.
            self.atualizar_tabela()

        except Exception as error:
            messagebox.showerror(
                "Erro",
                f"Não foi possível cadastrar:\n{error}"
            )


    # Lista os alunos cadastrados.
    def atualizar_tabela(self):

        # Remove os registros antigos da tabela visual.
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        # Busca os alunos no banco.
        alunos = listar()

        # Insere os registros na tabela.
        for aluno in alunos:

            self.tabela.insert(
                "",
                "end",
                values=(
                    aluno["id"],
                    aluno["nome"],
                    aluno["idade"],
                    f'{aluno["nota"]:.2f}'
                )
            )

        # Atualiza a média geral.
        media = media_geral()

        self.media_label.configure(
            text=f"Média geral: {media:.2f}"
        )


    # Busca um aluno pelo nome.
    def buscar_aluno(self):

        nome = self.busca_input.get().strip()

        if not nome:
            self.atualizar_tabela()
            return

        aluno = buscar(nome)

        # Limpa a tabela antes de mostrar o resultado.
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        if aluno:

            self.tabela.insert(
                "",
                "end",
                values=(
                    aluno["id"],
                    aluno["nome"],
                    aluno["idade"],
                    f'{aluno["nota"]:.2f}'
                )
            )

        else:
            messagebox.showinfo(
                "Busca",
                "Aluno não encontrado."
            )


    # Remove o aluno selecionado na tabela.
    def remover_aluno(self):

        selecionado = self.tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione um aluno na tabela."
            )
            return

        # Recupera os dados da linha selecionada.
        dados = self.tabela.item(selecionado[0])
        aluno_id = dados["values"][0]

        confirmar = messagebox.askyesno(
            "Confirmar",
            "Deseja realmente remover este aluno?"
        )

        if confirmar:

            remover(aluno_id)

            messagebox.showinfo(
                "Sucesso",
                "Aluno removido."
            )

            self.atualizar_tabela()

            # Limpa a pesquisa para voltar a mostrar todos.
            self.busca_input.delete(0, "end")
