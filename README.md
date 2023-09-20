# 🗞️ Spotnews

Aplicação feita de acordo com a arquitetura MTV (model, template, view). Com ela, é possíveil realizar operações CRUD em um banco de dados que modela notícias, autores e categorias. Páginas de formulários para o registro de novas notícias, categorias e usuários também foram desenvolvidas.

## Ferramentas Utilizadas
* Python
* Django
* Django Rest Framework
* Docker

## Como executar a aplicação
1. Clone o repositório.
2. Na raiz do projeto crie o ambiente virtual `python3 -m venv .venv`.
3. Ative o ambiente virtual `source .venv/bin/activate`.
4. Instale as dependências `python3 -m pip install -r dev-requirements.txt`.
6. Utilize os seguintes comandos para criar o banco.
 ```bash
  docker build -t spotnews-db .
  docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
  ```
7. Faça as migrações com `python3 manage.py migrate`.
8. Suba a aplicação usando `python3 manage.py runserver`.

## Detalhes do Desenvolvimento
