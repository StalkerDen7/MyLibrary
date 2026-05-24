from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Model
from models.books import BooksModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создаем таблицы при запуске приложения
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    yield
    # Здесь можно добавить код для очистки ресурсов при завершении приложения

app = FastAPI(lifespan=lifespan)

    