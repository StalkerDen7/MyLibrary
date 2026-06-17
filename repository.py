from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.books import BooksModel
from schemas.books import SBookAdd


class BookRepository:
    
    @classmethod
    async def add_one(cls, data: SBookAdd, session: AsyncSession) -> BooksModel:
        book_dict = data.model_dump()
        book = BooksModel(**book_dict)
        session.add(book)
        await session.commit()
        await session.refresh(book)

        return book
    
    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[BooksModel]:
        result = await session.execute(select(BooksModel))

        return result.scalars().all()
    
    @classmethod
    async def get_one(cls, book_id: int, session: AsyncSession) -> BooksModel | None:
        result = await session.execute(select(BooksModel).where(BooksModel.id == book_id))

        return result.scalar_one_or_none()
    
    @classmethod
    async def update_one(cls, book_id: int, data: SBookAdd, session: AsyncSession) -> BooksModel | None:
        book_dict = data.model_dump()
        await session.execute(update(BooksModel).where(BooksModel.id == book_id).values(**book_dict))
        await session.commit()

        return await cls.get_one(book_id, session)
    
    @classmethod
    async def delete_one(cls, book_id: int, session: AsyncSession) -> bool:
        result = await session.execute(delete(BooksModel).where(BooksModel.id == book_id))
        await session.commit()

        return result.rowcount > 0