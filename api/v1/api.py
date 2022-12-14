from fastapi import APIRouter
from api.v1.endpoints import livros


"""
É aqui que é feito os imports para montar API. 
Se tiver vários objetos em crud, importar para esse diretório.
"""


api_router = APIRouter()
api_router.include_router(livros.router, prefix='/livros_lidos', tags=["livros_lidos"]) # endpoint completo > /api/v1/livros_lidos


