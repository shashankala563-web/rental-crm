from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, List
import os
from . import models, schemas
from .routers import clients, users
from .database import engine, get_db, Session

# Create database tables
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