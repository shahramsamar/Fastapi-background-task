from typing import Union
from fastapi import FastAPI, BackgroundTasks


from time import sleep
import threading
from random import randint

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



""" this is a simple BackgroundTasks implementation"""


def trigger_process(num):
    print("Process triggered", num)
    sleep(randint(2, 10))
    print("Process finished", num)
    
num = 1


@app.get("/BackgroundTasks")
async def test_BackgroundTasks(background_tasks:BackgroundTasks):
    global num
    background_tasks.add_task(trigger_process, num)
    num += 1
    return {"detail": "done"}
