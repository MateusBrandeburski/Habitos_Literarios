from core.configs import settings
from sqlalchemy import Column, Integer, String
from typing import List



"""
Aqui é a comunicação com o banco de dados. SqlAchemy, POO do python com BD.
"""

# DBBaseMOdel = declarativebase()


class LivrosModel(settings.DBBaseModel):
    __tablename__ = 'livros_lidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200))
    genero = Column(String(200))
    numero_paginas = Column(Integer)
    ano = Column(Integer)

class ListaLivros(settings.DBBaseModel):
    __tablename__ = 'livros_lidos'
    livros = List[LivrosModel]



