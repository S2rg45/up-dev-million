from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Importing routes

from app.services.change_price.routes import change_route
from app.services.create_property.routes import create_route
from app.services.image_property.routes import image_routes

# Creating FastAPI instance
app = FastAPI(title="Million API", 
              description="API for Million", 
              version="1.0.0")

# CORS
origins = [
    "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# Including routes
app.include_router(change_route.router)
app.include_router(create_route.router)
app.include_router(image_routes.router)

# Running server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

