from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:karateka30@localhost:5432/habitos_literarios"

    DBBaseModel = declarative_base()

    class Config: 
        case_sensitive = True #manter tudo maiúsuco ou minúsculo



# Parece que isso de instânciar objeto, serve para usar uma classe em qualquer lugar
settings = Settings()

