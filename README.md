# Sistema de Gerenciamento de Biblioteca

Este é um sistema de gerenciamento de biblioteca desenvolvido utilizando Flask no backend em Python. Ele permite o cadastro e consulta eficientes de livros com operações CRUD (Create, Read, Update, Delete) via SQLAlchemy para interação segura com o banco de dados SQL.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Rotas da API](#rotas-da-api)
- [Templates HTML](#templates-html)

## Descrição do Projeto

Este sistema permite que os usuários realizem operações de cadastro, consulta, atualização e exclusão de livros em uma biblioteca. Utilizando Flask para o backend e SQLAlchemy para a interação com o banco de dados SQL, o sistema é eficiente e seguro.

## Funcionalidades

- Adicionar novos livros
- Consultar lista de livros
- Atualizar informações de livros existentes
- Remover livros do sistema

## Pré-requisitos

- Python 3.x
- Virtualenv

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-biblioteca.git
   cd sistema-biblioteca
   ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```
  
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1. No arquivo `config.py`, configure a URI do banco de dados:
    ```bash
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))
  
    class Config:
      SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
      SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

2. Execute as migrações do banco de dados:
    ```bash
    flask db init
    flask db migrate -m "create books table"
    flask db upgrade
    ```

## Como Usar

1. Inicie o servidor Flask:
    ```bash
    flask db init
    flask db migrate -m "create books table"
    flask db upgrade
    ```

2. Acesse o sistema no navegador em `http://127.0.0.1:5000`.

## Estrutura do Projeto
```
biblioteca/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ └── forms.py
├── migrations/
├── templates/
│ ├── index.html
│ ├── new_book.html
│ └── edit_book.html
├── config.py
├── run.py
└── requirements.txt
```

## Rotas da API
* `GET /` - Lista todos os livros
* `GET /book/new` - Formulário para adicionar um novo livro
* `POST /book/new` - Adiciona um novo livro
* `GET /book/<int:id>/edit` - Formulário para editar um livro existente
* `POST /book/<int:id>/edit` - Atualiza um livro existente
* `POST /book/<int:id>/delete` - Remove um livro

## Templates HTML
* `index.html` - Página inicial que lista todos os livros
* `new_book.html` - Formulário para adicionar um novo livro
* `edit_book.html` - Formulário para editar um livro existente

