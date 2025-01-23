

# main.py

import models.
from pydantic import BaseModel, conlist
from typing import List
from fastapi import FastAPI, Body
from joblib import load


class steel(BaseModel):
    data: List[conlist(float, min_items=13, max_items=13)]
    clf = None

app = FastAPI(Title = 'Steel Tempering Predictor', 
              description = 'A tool to predict the tempering tempering to reach a desired final hardness for a given steel composition and tempering time',
              version = '1.0')

@app.on_event('startup')
async def load_model():
    model = load('models/tempering_hardness_gbr.joblib')


@app.get("/")
async def root():
    return {"message": "Hello World"}
