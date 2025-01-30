
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings

class Mongo():
    def __init__(self) -> None:
        self.client = AsyncIOMotorClient(settings.DATABASE_URL)
        self.database = self.client.get_database("ProjetoDIO")
    

    def get(self) -> AsyncIOMotorClient:
        return self.client
    
    def get_database(self):
        return self.database


mongodb = Mongo()
