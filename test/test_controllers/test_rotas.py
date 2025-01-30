from typing import List
from src.fixture import produto
from http import HTTPStatus

async def test_controller_produto_create_success(client, produto_rota):
    response = await client.post(produto_rota, json = produto)

    assert response.status_code == HTTPStatus.CREATED


async def test_controller_produto_get_success(client, produto_rota, produto_inserted):
    response = await client.get(f"{produto_rota}{produto_inserted.id}")

    assert response.status_code == HTTPStatus.CREATED


async def test_controller_produto_get_not_found(client, produto_rota):
    response = await client.get(f"{produto_rota}aabc-2345xpkj234-vvb678")

    assert response.status_code == HTTPStatus.NOT_FOUND


async def test_controller_produto_query_success(client, produto_rota, produto_inserted):
    response = await client.get(produto_rota)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json, List)
    assert len(response.json()) > 1


async def test_controller_produto_update_success(client, produto_rota, produto_inserted):
    response = await client.patch(f"{produto_rota}{produto_inserted.id}", json = {"quantidade":50})

    assert response.status_code == HTTPStatus.OK


async def test_controller_produto_delete_no_content(client, produto_rota, produto_inserted):
    response = await client.patch(f"{produto_rota}{produto_inserted.id}", json = {"quantidade":50})
    
    assert response.status_code == HTTPStatus.NO_CONTENT


async def test_controller_produto_delete_not_found(client, produto_rota):
    response = await client.delete(f"{produto_rota}aabc-2345xpkj234-vvb678")

    assert response.status_code == HTTPStatus.NOT_FOUND