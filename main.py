# %%
# imports
import os
from crud import CRUD
from dotenv import load_dotenv
from relacoes import Livro
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import exceptions as ex
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import PendingRollbackError
load_dotenv()

# %%
# Conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")
url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

livro_crud = CRUD(session)

# %%
# criando livros
try:
    livro_crud.create(
        isbn="9788521630814",
        titulo="Introdução à Computação Usando Python",
        autor="PERKOVIC, L.",
        ano_publicacao=2016,
        genero="Programação",
    )
except IntegrityError:
    print('Livro já cadastrado')
    session.rollback()
# %%
# Lendo registros como lista de objetos
try:
    livro = livro_crud.read("9788521630814")
except ex.NotFound as nf:
    print(nf)

# %%
# atualizando um registro
try:
    livro_crud.update(
        isbn='9788521630814',
        titulo="Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações",
        ano_publicacao=2018,
    )
except IntegrityError:
    print('O ano de publicação do livro deve ser maior que Zero')
    session.rollback()

except ex.NotFound as nf:
    print(nf)

# %%
# removendo um registro
try:
    livro_crud.delete(isbn="9788521630814")
except:
    print('O livro não existe, então não pode ser deletado.')

# %%
# encerrando a sessão com o banco de dados
session.close()
