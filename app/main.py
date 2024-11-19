
#!/usr/bin/env python3


import mysql.connector


from mysql.connector import Error
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "uwg9at"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

@app.get("/")  # zone apex
def zone_apex():
    return {"Good day": "sunshine"}


@app.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        #db.close()
        return(json_data)
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}
@app.get('/songs')
def get_songs():
    query = "SELECT s.title, s.album, s.artist, s.year, s.file, g.genre AS genre FROM songs s JOIN genres g WHERE s.genre = g.genreid;" 
    try:
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
#        db.close()
        return(json_data)
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}

# @app.get("/add/{a}/{b}")
#def add(a: int, b: int):
 #  return {"sum": a + b}


#@app.get("/multiply/{c}/{d}")
#def multiply(c: int, d:int):
#    return {"product": c*d}
# @app.get("/add/{a}/{b}")
#def add(a: int, b: int):
 #  return {"sum": a + b}


#@app.get("/multiply/{c}/{d}")
#def multiply(c: int, d:int):
#    return {"product": c*d}


# @app.get("/add/{a}/{b}")
#def add(a: int, b: int):
 #  return {"sum": a + b}


#@app.get("/multiply/{c}/{d}")
#def multiply(c: int, d:int):
#    return {"product": c*d}


#@app.get("/square/")
#def square(a: int):
#    return {"square": a * a}


#@app.get("/sayHello/")
#def hello():
#    return {"hello"}

