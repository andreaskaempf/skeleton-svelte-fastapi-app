# Backend server for the data driven dashboard

import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the app
app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Root query, does nothing
@app.get('/')
def index():
    return {'status': 'ok'}

# Simple API query
@app.get('/query')
def query():
    return {'time': time.time()}

