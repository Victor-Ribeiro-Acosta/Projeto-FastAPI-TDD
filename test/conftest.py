import asyncio
import pytest
from src.database.mongo import mongodb
from src.schemas.schemaProduto import ProdutoIn, ProdutoUpdate
from src.fixture import produto, produtos
from src.usercases.product_usercase import product_usercase
from httpx import AsyncClient
import uuid



@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()



def get_mongo():
    return mongodb.client


@pytest.fixture(autouse=True)
async def clear_collection():
    yield
    collection_names = await get_mongo().get_database("ProdutosDB").list_collection_name() 
    for collection in collection_names:
        if collection.startswith("system"):
            continue

        await get_mongo.get_database("ProdutosDB")[collection].delete_many()



@pytest.fixture
async def client() -> AsyncClient: # type: ignore
    from src.main import app

    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac



@pytest.fixture
def produto_rota() -> str:
    return "/produtos/"


@pytest.fixture
def id():
    return uuid.uuid4()


@pytest.fixture
def produto_in(id):
    return ProdutoIn(**produto, id=id)


@pytest.fixture
def produto_up(id):
    return ProdutoUpdate(**produto, id=id)


@pytest.fixture
async def produto_inserted(produto_in):
    await product_usercase.create(body = produto_in)


@pytest.fixture
def produtos_in():
    return [ProdutoIn(**produto, id=uuid.uuid4) for produto in produtos]


@pytest.fixture
async def produtos_inserted(produtos_in):
    return [await product_usercase.create(body = produto_in) for produto_in in produtos_in]