from typing import Union

from fastapi import FastAPI

esrp = FastAPI()


@esrp.get("/")
def get_root():
    return {"Hello": "bofa"}
