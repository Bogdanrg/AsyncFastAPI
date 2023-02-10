from fastapi import FastAPI
from core.db import db


def start():
    db.init()
    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    return app


app = start()
