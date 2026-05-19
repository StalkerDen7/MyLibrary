from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

# 1. Настройка URL
# Файл library.db создастся в корне проекта
DATABASE_URL = "sqlite+aiosqlite:///library.db"

# 2. Создание движка
engine = create_async_engine(DATABASE_URL)

# 3. Создание фабрики сессий
new_session = async_sessionmaker(engine, expire_on_commit=False)

# 4. Базовый класс для моделей
# MappedAsDataclass - нужен для удобной работы с типами (новинка 2.0)
class Model(MappedAsDataclass, DeclarativeBase):
    pass