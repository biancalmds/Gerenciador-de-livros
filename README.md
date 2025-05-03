
# 📚 Gerenciador de Livros

Este é um projeto acadêmico desenvolvido para praticar os conceitos de CRUD (Create, Read, Update, Delete) em Python, utilizando a biblioteca SQLAlchemy como ORM (Object Relational Mapper). A aplicação realiza o gerenciamento de uma tabela de livros em um banco de dados relacional.
## ✅ Funcionalidades

- Cadastrar livros com as seguintes informações:
  - ISBN (chave primária);
  - Título;
  - Autor;
  - Ano de publicação;
  - Gênero (opcional).

- Listar todos os livros cadastrados;
- Atualizar os dados de um livro existente;
- Remover um livro do banco de dados;
- Tratamento de erros para garantir integridade dos dados.
## 💻 Tecnologias e bibliotecas utilizadas

- Python 3.10+
- SQLAlchemy
- SQL Server (pode ser substituído por outro banco relacional)
- [requirements.txt](./requirements.txt) com todas as dependências
## 💻 Como executar

#### 1. Clone o repositório:

```bash
git clone https://github.com/biancalmds/Gerenciador-de-livros.git
cd Gerenciador-de-livros
```

#### 2. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

#### 3. Adicione as seguintes variáveis de ambiente no seu .env:

`HOST`

`BANCO_DE_DADOS`

`USUARIO`

`SENHA`

#### 4. Execute o arquivo principal para iniciar a aplicação:

```bash
python main.py
```
## 📦 Estrutura dos arquivos

```
.
├── crud.py          # Implementação das funções CRUD
├── exceptions.py    # Criação de exceção
├── main.py          # Conexão com o BD + execução do sistema com tratamento de exceções
├── relacoes.py      # Modelo da tabela de livros
├── requirements.txt # Lista de dependências
```
## 👨‍💻 Autores

Desenvolvido por [@biancalmds](https://github.com/biancalmds) e [@felipefpinto](https://github.com/felipefpinto) como parte de uma atividade acadêmica no curso de Sistemas de Informação.
