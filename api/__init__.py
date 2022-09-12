from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core import models
from core.database import SessionLocal, engine
from core.schemas.user_schema import UserCreate
from utils.crud_users import create_user

from .v1 import v1_router


def create_app():
    models.Base.metadata.create_all(bind=engine)

    app = FastAPI(title="haggling")  # description=core.setting.DESC)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # core.setting.ORIGINS,  #TODO
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(v1_router)

    @app.on_event("startup")
    def startup_populate_db():
        db = SessionLocal()

        if db.query(models.User).count() == 0:
            users = [UserCreate(username="batman"), UserCreate(username="superman")]
            for user in users:
                create_user(db, user)

    return app
