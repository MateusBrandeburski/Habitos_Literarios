from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.livros_models import LivrosModel
from schemas.livros_schema import LivrosSchema
from core.deps import get_session

router = APIRouter()


@router.post('/', response_model=LivrosSchema) # (devolve)livros Schemas, pydantic pega esse objeto schema e converte para Json... Talvez fosse o casso de passar uma List 
async def post_livros(livros: LivrosSchema, db: AsyncSession = Depends(get_session)): # retorno
    
    novos_livros = LivrosModel(nome=livros.nome, genero=livros.genero,
                                numero_paginas=livros.numero_paginas,
                                ano=livros.ano)

    db.add(novos_livros) # db recebe
    await db.commit() # salva

    return novos_livros 


@router.get('/', response_model=List[LivrosSchema]) # devolve uma lista de livros
async def get_livros(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(LivrosModel) # essa query, talvez me dê uma pista de como fazer...
        result = await session.execute(query)
        livros: List[LivrosModel] = result.scalars().all()

        return livros


