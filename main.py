# //react/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"]
)
 
@app.get('/get_data')
async def get_data():
    return {'body': 'Hello World from python fastapi'}