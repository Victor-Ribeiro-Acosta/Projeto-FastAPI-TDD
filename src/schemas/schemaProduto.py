from typing import Annotated, Optional
from bson import Decimal128
from uuid import uuid4
from pydantic import AfterValidator, BaseModel, PositiveInt, Field, UUID4, model_serializer, model_validator
from decimal import Decimal

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True
    

class OutSchema(BaseModel):
    id: UUID4 = Field()
    
    @model_validator(mode='before')
    def set_schema(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))
        return data


class Produto(BaseModel):
    nome: str = Field(...)
    preco: Decimal = Field(...)
    quantidade: PositiveInt = Field(...)
    categoria: str = Field(...)


class ProdutoIn(BaseSchema,Produto):
    ...


class ProdutoOut(ProdutoIn, OutSchema):
    ...


def convert_decimal128(v):
    return Decimal128(str(v))

_decimal = Annotated[Decimal, AfterValidator(convert_decimal128)]


class ProdutoUpdate(Produto, BaseSchema):
    preco: Optional[_decimal] = Field(None)
    quantidade: Optional[PositiveInt] = Field(None)
    categoria: Optional[str] = Field(None)


class ProdutoUpdateOut(ProdutoOut):
    ...