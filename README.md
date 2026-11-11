# Projeto-Mafra-matricula

Projeto acadêmico desenvolvido para a disciplina de Coding, ministrada pela professora Mafra. O projeto contém um sistema de gerenciamento de alunos desenvolvido em Python, com interface gráfica e armazenamento local utilizando SQLite.

## Integrantes

1. Gustavo Nascimento da Silva — 01866201
2. Thiago Henrique Pereira — 01892849
3. Matheus Augusto Gomes da Silva — 01894714
4. Kauãn Felipe da Silva Melo — 01892125
5. Guilherme Fortaleza de Sousa — 01877047

## Funções dos alunos

- **Gustavo:** Leitura e interpretação do PDF e organização das funções de cada aluno.
- **Thiago:** Criação do repositório e documentação do código.
- **Matheus:** Revisão final e teste completo do código.
- **Kauãn:** Desenvolvimento do código.
- **Guilherme:** Desenvolvimento do código.

---

## Tecnologias utilizadas

- Python
- CustomTkinter — Interface gráfica.
- SQLite — Banco de dados local.

## Funcionalidades

- Cadastro de alunos.
- Listagem de alunos cadastrados.
- Busca de alunos pelo nome.
- Remoção de alunos.
- Cálculo da média geral das notas.
- Armazenamento permanente dos dados em banco SQLite.

---

## Como executar o projeto

### 1. Pré-requisitos

É necessário ter o Python 3 instalado no computador.

Verifique a instalação:

```bash
python --version
```

No Linux, caso o Tkinter não esteja instalado, instale-o utilizando o gerenciador de pacotes da sua distribuição.

No CachyOS/Arch Linux:

```bash
sudo pacman -S tk
```

### 2. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd Projeto-Mafra-matricula
```

### 3. Criar o ambiente virtual

O ambiente virtual permite instalar as dependências do projeto sem modificar o Python do sistema.

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

**Linux (Bash/Zsh):**

```bash
source venv/bin/activate
```

**Linux (Fish):**

```fish
source venv/bin/activate.fish
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

### 6. Iniciar o sistema

Execute:

```bash
python main.py
```

Pronto! A interface gráfica do sistema será aberta.

O banco de dados SQLite (`matriculas.db`) é criado automaticamente na primeira execução, sem necessidade de configuração manual.

---

## Banco de dados

O projeto utiliza SQLite, que permite armazenar os dados localmente sem precisar instalar ou configurar um servidor de banco de dados.

O arquivo `matriculas.db` é gerado automaticamente durante a inicialização do sistema e mantém os alunos cadastrados mesmo após o encerramento do programa.

**Observação:** o banco é local e independente em cada computador. Os dados cadastrados não são compartilhados entre os integrantes pelo GitHub.

---

## Encerramento

Projeto desenvolvido como atividade acadêmica da disciplina de Coding, com o objetivo de aplicar conhecimentos de programação Python, organização de código, interfaces gráficas e manipulação de banco de dados.