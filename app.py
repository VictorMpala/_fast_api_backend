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

@app.get('/')
def home():
    return {'body':'This is the home directory'}

@app.get('/get_data')
async def get_data():
    return {'body': 'Hello World from python fastapi'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
