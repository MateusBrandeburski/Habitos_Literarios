from core.configs import settings
from core.database import engine

async def create_tables() -> None:
    from models.livros_models import LivrosModel
    print('Criando as tabelas no BD...')


    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)  #exclui tabelas
        await conn.run_sync(settings.DBBaseModel.metadata.create_all) # cria novas 'por cima'
    print('tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())