from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(t: Optional[str]):
    # return {"Hello": "World"}
    return {"Hello": t}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}