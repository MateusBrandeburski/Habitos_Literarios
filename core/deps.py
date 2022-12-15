# juntar todas as dependdecias que se cria na aplicação

from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
        #print('sessão/banco de dados aberta, mas não fechada...')