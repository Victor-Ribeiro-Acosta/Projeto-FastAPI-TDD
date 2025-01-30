from fastapi import APIRouter, Body, Depends, HTTPException, Path
from http import HTTPStatus

from pydantic import UUID4
from src.schemas.schemaProduto import ProdutoIn, ProdutoOut, ProdutoUpdate, ProdutoUpdateOut
from src.core.exceptions import NotFoundError
from src.usercases.product_usercase import ProductUsercase

rota = APIRouter(tags=["produtos"])

@rota.post(path="/", status_code=HTTPStatus.CREATED)
async def post(
    body: ProdutoIn = Body(...),
    usercase: ProductUsercase = Depends()) -> ProdutoOut:

    return await usercase.create(body=body)


@rota.get(path="/{id}", status_code=HTTPStatus.OK)
async def get(
    id: UUID4 = Path(alias='id'),
    usercase: ProductUsercase = Depends()):

    try:
        return await usercase.get(id=id)
    except NotFoundError as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=exc.message)


@rota.get(path="/{id}", status_code=HTTPStatus.OK)
async def query(usercase: ProductUsercase = Depends()):
    return await usercase.query()


@rota.patch(path="/{id}", status_code=HTTPStatus.OK)
async def patch(
    id: UUID4 = Path(alias='id'),
    body: ProdutoUpdate = Body(...),
    usercase: ProductUsercase = Depends()) -> ProdutoUpdateOut:

    return await usercase.update(id=id, body=body)


@rota.delete(path="/{id}", status_code=HTTPStatus.NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias='id'),
    usercase: ProductUsercase = Depends()):

    try:
        await usercase.delete(id=id)
    except NotFoundError as exc:
        return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=exc.message)