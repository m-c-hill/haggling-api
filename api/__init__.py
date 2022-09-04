from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# from tortoise.contrib.fastapi import register_tortoise

from .v1 import v1_router


def create_app():
    app = FastAPI(title="apiAutoTestWeb") #description=core.setting.DESC)

    # register_tortoise(
    #     app,
    #     db_url="sqlite://db.sqlite3",
    #     modules={"models": ["db.models"]},
    #     # # 生成表
    #     generate_schemas=True,
    #     # # 使用异常，当无数据是自动返回
    #     # add_exception_handlers=True,
    # )

    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",  # core.setting.ORIGINS,  #TODO
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(v1_router)

    @app.get("/")
    def home():
        return "Hello"

    return app
