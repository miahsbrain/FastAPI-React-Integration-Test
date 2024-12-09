import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI(debug=True)

origins = [
    "http://localhost:3000"
]

CORSMiddleware(app=app, allow_origins=origins, allow_credentials=True, allow_headers=['*'], allow_methods=['*'])

class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

memory_db = {'fruits': []}

@app.get('/')
def index():
    return {'message': 'Working, go to /fruits'}

@app.get('/fruits', response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db['fruits'])

@app.post('/fruits', response_model=Fruit)
def add_fruits(fruit: Fruit):
    memory_db['fruits'].append(fruit)
    return fruit

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)