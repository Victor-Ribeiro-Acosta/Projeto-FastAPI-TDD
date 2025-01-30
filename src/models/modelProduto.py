from src.models.models import Base
from src.schemas.schemaProduto import ProdutoIn

class Produto(Base, ProdutoIn):
    ...
