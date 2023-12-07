from fastapi import FastAPI
from .models import models
from .config.database import engine
from .routers import orders, user, recipe, auth, product, recommendation
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Starter",
    description="A starter template for FastAPI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(orders.router)
app.include_router(user.router)
app.include_router(recipe.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(recommendation.router)

@app.get("/")
def root():
    return {"message": "Hello"}