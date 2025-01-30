from typing import List
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.database.mongo import mongodb
from src.schemas.schemaProduto import ProdutoIn, ProdutoOut, ProdutoUpdate, ProdutoUpdateOut
from src.core.exceptions import NotFoundError
from uuid import UUID, uuid4
import pymongo
from src.models.modelProduto import Produto

class ProductUsercase:
    def __init__(self):
        self.client: AsyncIOMotorClient = mongodb.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("produtos")
    
    async def create(self, body: ProdutoIn) -> ProdutoOut:
        produto = Produto(**body.model_dump())
        await self.collection.insert_one(produto.model_dump())

        return ProdutoOut(**produto.model_dump())
    


    async def get(self, id: UUID) -> ProdutoOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundError(message=f"Não há produto cadastrado no id {id}")
        
        return ProdutoOut(**result)



    async def query(self) -> List[ProdutoOut]:
        return [ProdutoOut(**item) async for item in self.collection.find()]



    async def update(self, id: UUID, body: ProdutoUpdate) -> ProdutoUpdateOut:
        produto = ProdutoUpdateOut(**body.model_dump(exclude_none=True))
        result = self.collection.find_one_and_update(filter = {"id": id},
                                                     update = {"$set": produto.model_dump()},
                                                     return_document = pymongo.ReturnDocument.AFTER
                                                     )
        return ProdutoUpdateOut(**result)



    async def delete(self, id:UUID) -> bool:
        # produrar produto
        produto = await self.collection.find_one({"id": id})
        # retornar erro se produto não for encontrado
        if not produto:
            raise NotFoundError(message=f"Não há produto cadastrado no id {id}")
    
        # deletar produto
        result = self.collection.delete_one({"id": id})
        return True if result.deleted_count > 0 else False



product_usercase = ProductUsercase()