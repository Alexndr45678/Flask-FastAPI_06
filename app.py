import uvicorn
from fastapi import FastAPI
from store_db import database
from routers.users import router as router_users
from routers.items import router as router_items
from routers.orders import router as router_orders

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router_users, tags=["users"])
app.include_router(router_items, tags=["items"])
app.include_router(router_orders, tags=["orders"])

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
