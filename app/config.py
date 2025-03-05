from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    POSTGRES_USER: str = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
    POSTGRES_PORT: str = os.environ['POSTGRES_PORT']
    POSTGRES_DB: str = os.environ['POSTGRES_DB']
    POSTGRES_HOST: str = os.environ['POSTGRES_HOST']

    VRM_TOKEN: str = os.environ['VRM_Ttoken']
    VRM_Instalacion: str = os.environ['VRM_Instalacion']

    class Config:
        env_file = 'settings.cfg'

settings = Settings()