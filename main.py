from typing import Union
from fastapi import FastAPI


from time import sleep
import threading

app = FastAPI()

""" this is a simple sleep implementation"""
@app.get("/sleep")
async def test_sleep():
    sleep(5)
    return {"detail": "done"}


