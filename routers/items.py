from fastapi import APIRouter, HTTPException
from store_db import database, items
from models.items import Item, ItemIn


router = APIRouter()


@router.get("/items/", response_model=list[Item])
async def get_items():
    items_ = items.select()
    return await database.fetch_all(items_)


@router.post("/items/")
async def add_item(item: ItemIn):
    query = items.insert().values(
        name=item.name, description=item.description, price=item.price
    )
    await database.execute(query)
    return {"msg": "Item added"}


@router.get("/items/{id}", response_model=Item)
async def get_item(id: int):
    query = items.select().where(items.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/items/{id}", response_model=Item)
async def update_item(id: int, item: ItemIn):
    query = items.update().where(items.c.id == id).values(**item.model_dump())
    result = await database.execute(query)
    if result:
        return {**item.model_dump(), "id": id}
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/items/")
async def delete_item(id: int):
    query = items.delete().where(items.c.id == id)
    result = await database.execute(query)
    if result:
        return {"msg": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
