from typing import Optional
from pydantic import BaseModel as SchemaCBaseModel


"""
Aqui são os dados que são colocados na API

Em models, é a comunicação com com banco de dados.

Schema = pydantic > json
Models = sqlalchemy > dados

"""



class LivrosSchema(SchemaCBaseModel):

    id: Optional[int]
    nome: str
    genero: str
    numero_paginas: int
    ano: int

    class Config:
        orm_mode = True



            
            
