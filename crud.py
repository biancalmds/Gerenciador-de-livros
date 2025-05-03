import pandas as pd
from relacoes import Livro
from sqlalchemy.orm import Session
import exceptions as ex


class CRUD:
    def __init__(self, session: Session):
        self.__session = session

    def create(self, isbn, titulo, autor, ano_publicacao, genero=None):
        livro = Livro(isbn=isbn, titulo=titulo, autor=autor, ano_publicacao=ano_publicacao, genero=genero)
        self.__session.add(livro)
        self.__session.commit()
        
    def read(self, isbn=None):
       livro = self.__session.query(Livro).filter_by(isbn=isbn).first()
       if livro:   
        return livro
       else:
            raise ex.NotFound('Livro não encontrado')
       
    def update(self, isbn, titulo=None, autor=None, ano_publicacao=None, genero=None):
        livro_atualizado = self.__session.query(Livro).filter_by(isbn=isbn).one_or_none()
        if livro_atualizado:
            if titulo != None:
                livro_atualizado.titulo = titulo
            if autor != None:
                livro_atualizado.autor = autor
            if ano_publicacao != None:
                livro_atualizado.ano_publicacao = ano_publicacao
            if genero != None:
                livro_atualizado.genero = genero
            self.__session.commit()
        else:
            raise ex.NotFound('Livro não encontrado')

    def delete(self, isbn):
       livro_deletado = self.__session.query(Livro).filter_by(isbn=isbn).first()
       self.__session.delete(livro_deletado)
       self.__session.commit()

          

