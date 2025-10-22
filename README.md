# Ecommerce API Criada com Flask

## Descrição
A **Ecommerce API** é um sistema backend desenvolvido com **Flask** para gerenciar produtos, usuários e carrinhos de compras. Suas funcionalidades incluem **autenticação**, operações **CRUD** para produtos, manipulação de itens do carrinho, e checkout.

## Tecnologias Usadas

![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/FLASK-000000?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLITE-003B57?style=for-the-badge&logo=sqlite&logoColor=white) ![Postman](https://img.shields.io/badge/POSTMAN-FF6C37?style=for-the-badge&logo=postman&logoColor=white) 

## Funcionalidades
- **Autenticação**:
  - Login de usuários.
  - Logout de usuários.
- **Produtos**:
  - Criar, listar, detalhar, atualizar e deletar produtos.
- **Carrinho de Compras**:
  - Adicionar e remover itens do carrinho.
  - Visualizar o conteúdo do carrinho.
  - Realizar "checkout", esvaziando o carrinho.
- **EndPoints Públicos e Protegidos**:
  - Autenticação para proteger ações como adicionar, deletar ou atualizar produtos e itens do carrinho.

## Estrutura do Projeto
- **app.py**: Arquivo principal que contém as rotas e a lógica.
- **requirements.txt**: Lista das dependências.
- **.gitignore**: Define os diretórios que devem ser ignorados pelo Git.

##  Endpoints

###  Usuários:
- **POST /register**: Cria um usuário com nome e senha.

###  Autenticação:
- **POST /login**: Faz login de um usuário.
- **POST /logout**: Faz logout de um usuário autenticado.

### Produtos:
- **POST /api/products/add**: Adiciona um novo produto (protegido).
- **GET /api/products**: Lista todos os produtos.
- **GET /api/products/{id}**: Detalha um produto específico.
- **PUT /api/update/{id}**: Atualiza os dados de um produto (protegido).
- **DELETE /api/products/delete/{id}**: Remove um produto (protegido).

### Carrinho de Compras:
- **POST /api/cart/add/{id}**: Adiciona um item ao carrinho (protegido).
- **DELETE /api/cart/remove/{id}**: Remove um item do carrinho (protegido).
- **GET /api/cart**: Exibe os itens no carrinho (protegido).
- **POST /api/cart/checkout**: Realiza o checkout, esvaziando o carrinho (protegido).

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/DanilloSouza03/ecommerce-api.git
   cd ecommerce-api
2. Crie o arquivo .env a partir do exemplo:
   ```bash
    copy .env.example .env   # Windows
    cp .env.example .env # ou no Linux/macOS
3. Instale o Poetry:
   ```bash
    pip install poetry
4. Crie e ative o ambiente virtual com Poetry
    ```bash
    poetry install      # Cria o ambiente virtual e instala as dependências
    poetry env activate
5. Execute a aplicação:
   ```bash
    flask --app src.app run 
    flask --app src.app run --debug # Aqui já com o modo debug

## Testando a API com Postman

O projeto inclui uma coleção do Postman para facilitar os testes da API.

1. Abra o [Postman](https://www.postman.com/).
2. Vá em **File > Import**.
3. Selecione o arquivo localizado em: `postman/Ecommerce-API.postman_collection.json`

<hr>
<p align="center">
👨‍💻 @dev.danillo
</p>