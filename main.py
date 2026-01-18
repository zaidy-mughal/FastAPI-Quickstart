from fastapi import FastAPI
from fastapi import Query
from typing import Optional, Annotated
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: int):
    return {"message": f"Hello {name}"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: Optional[int] = None, limit: Optional[int]= None):
    if skip is None:
        skip = 0
    if limit is None:
        limit = 1
    return fake_items_db[skip: skip + limit]


#Pydantic Model for request body validation
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# path parameter, request body and query parameters in FastAPI.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


# additional validation using Query with Annotated.
@app.get("/products/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

