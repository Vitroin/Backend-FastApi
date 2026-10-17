from contextlib import asynccontextmanager

from fastapi import FastAPI

from .routers import coaching_tips, health, video_analysis



app = FastAPI()

#Registers the routers
app.include_router(health.router)
app.include_router(video_analysis.router)
app.include_router(coaching_tips.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
