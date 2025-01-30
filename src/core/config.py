from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Cadastro de produtos'
    ROOT_PATH: str = "/"
    DATABASE_URL: str = "mongodb+srv://victor:mdb2024@projetodio.xhba37y.mongodb.net/ProdutosDB?retryWrites=true&w=majority&appName=ProjetoDIO"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()