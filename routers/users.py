from fastapi import APIRouter, HTTPException
from store_db import users, database
from models.users import User, UserIn


router = APIRouter()


@router.get("/users/", response_model=list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@router.post("/users/")
async def add_user(user: UserIn):
    query = users.insert().values(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
    )
    await database.execute(query)
    return {"msg": "User added"}


@router.get("/users/{id}", response_model=User)
async def get_users(id: int):
    query = users.select().where(users.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{id}", response_model=User)
async def update_user(id: int, user: UserIn):
    query = (
        users.update()
        .where(users.c.id == id)
        .values(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
        )
    )
    # user_ = await database.fetch_one(query)
    result = await database.execute(query)
    if result:
        return {**user.dict(), "id": id}
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/")
async def delete_user(id: int):
    query = users.delete().where(users.c.id == id)
    result = await database.execute(query)
    if result:
        return {"msg": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
