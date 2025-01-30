from src.schemas.schemaProduto import ProdutoIn
from src.fixture import produto
import uuid
import pytest
from pydantic import ValidationError

def test_schema_produto_sucesso():

    cadastro = ProdutoIn(**produto, id=uuid.uuid4())
    assert produto['nome'] == cadastro.nome
    #assert type(produto['preco']) == type(cadastro.preco)

def test_schemas_produto_falha():

    produto = {'nome': 'Xiaomi Redmi 13', 'preco': '800.0', 'quantidade': 30, 'categoria': 'Celulares e smartfones'}
    with pytest.raises(ValidationError) as err:
        ProdutoIn().model_validate(produto)
    assert err.value.errors()[0] =={'type': 'missing', 'loc': ('nome',), 'msg': 'Field required', 'input': {}, 'url': 'https://errors.pydantic.dev/2.10/v/missing'}