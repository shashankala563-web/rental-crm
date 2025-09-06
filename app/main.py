from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, List
import psycopg
from psycopg.rows import dict_row
import time
from . import models, schemas
from .routers import clients, users
from .database import engine, get_db, Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rental CRM API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(clients.router)

# Database connection
while True:
    try:
    # Connect using connection string
        conn = psycopg.connect(host = 'localhost',dbname = 'fastapi',user = 'postgres',password = '123456789')
        cursor = conn.cursor(row_factory=dict_row)
        print("Database Connection Successful") 
        break
    except Exception as error:
        print(" Database Connection Failed\nError:", error)
        time.sleep(3)

# Serve HTML pages
@app.get("/")
def serve_home():
    return FileResponse("static/index.html")

@app.get("/login")
def serve_login():
    return FileResponse("static/login.html")

@app.get("/signup")
def serve_signup():
    return FileResponse("static/signup.html")

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse("static/dashboard.html")

# Mount static files for CSS/JS
app.mount("/static", StaticFiles(directory="static"), name="static")