from src.core.exceptions import NotFoundError
from src.usercases.product_usercase import product_usercase
from src.schemas.schemaProduto import ProdutoOut, ProdutoUpdateOut
import pytest


async def test_usercases_create_success(produto_in):
    result = await product_usercase.create(body = produto_in)

    assert isinstance(result, ProdutoOut)
    assert result.nome == produto_in.nome



async def test_usercases_get_success(produto_inserted):
    result = await product_usercase.get(id = produto_inserted.id)

    assert isinstance(result, ProdutoOut)



async def test_usercases_get_not_found():
    with pytest.raises(NotFoundError) as err:
        result = await product_usercase.get(id = "abc23fjz45699xpk00")


    assert isinstance(result, ProdutoOut)
    assert err.value.errors[0] == f"Não há produto cadastrado no id {id}"


async def test_usercases_query_success():
    result = await product_usercase.query()

    assert isinstance(result, list)
    assert len(result) > 1


async def test_usercases_update_success(produto_inserted, produto_up):
    produto_up.preco = "9.300"
    result = await product_usercase.update(id = produto_inserted.id, body = produto_up)

    assert isinstance(result, ProdutoUpdateOut)


async def test_usercases_delete_success(produto_inserted):
    result = await product_usercase.delete(id = produto_inserted.id)