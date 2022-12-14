from core.configs import settings
from sqlalchemy import Column, Integer, String



"""
Aqui é a comunicação com o banco de dados. SqlAchemy, POO do python com BD.
"""

# DBBaseMOdel = declarativebase()


class LivrosModel(settings.DBBaseModel):
    __tablename__ = 'livros_lidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    genero = Column(String(20))
    numero_paginas = Column(Integer)
    ano = Column(Integer)


