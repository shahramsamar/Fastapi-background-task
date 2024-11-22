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


""" this is a simple async implementation"""

def trigger_process():
    print("Process triggered")
    sleep(10)
    print("Process finished")
    

@app.get("/async")
async def test_async():
    task =threading.Thread(target=trigger_process)
    task.start()
    return {"detail": "done"}
