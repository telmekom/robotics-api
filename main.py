from typing import Union

from fastapi import FastAPI

from routers import shops, robots


app = FastAPI()
app.include_router(shops.router)
app.include_router(robots.router)

@app.get("/healthcheck", description="Basic server availability check")
def health_check():
    return {
        "endpoint": "/healthcheck",
        "success" : True,
    }
