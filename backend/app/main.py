from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.predict import router

app = FastAPI(title="CIFAR-10 Image Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
