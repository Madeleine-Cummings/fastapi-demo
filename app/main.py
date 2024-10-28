#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Good day": "sunshine"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

<<<<<<< HEAD
@app.get("/multiply/{c}/{d}")
def multiply(c: int, d:int):
    return {"product": c*d}

=======
@app.get("/square/")
def square(a: int):
    return {"square": a * a}
>>>>>>> 0ba4cefc11bb552bca0359f7756590d2e078da99


@app.get("/sayHello/{a}")
def hello():
    return {"hello"}

