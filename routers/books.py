from fastapi import APIRouter, HTTPException, status
from typing import Annotated
from database import SessionDependency
from schemas.books import SBookAdd, SBook
from repository import BookRepository


router = APIRouter(prefix="/books", tags=["книги"])

@router.post("", response_model=SBook)
async def add_book(data: SBookAdd, session: SessionDependency):
    book_model = await BookRepository.add_one(data, session)

    return book_model


@router.get("", response_model=list[SBook])
async def get_books(session: SessionDependency):
    books = await BookRepository.get_all(session)

    return books


@router.get("/{book_id}", response_model=SBook)
async def get_book(book_id: int, session: SessionDependency):
    book = await BookRepository.get_one(book_id, session)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга по ID {book_id} не найдена")

    return book


@router.put("/{book_id}", response_model=SBook)
async def update_book(book_id: int, data: SBookAdd, session: SessionDependency):
    book = await BookRepository.update_one(book_id, data, session)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга по ID {book_id} не найдена")

    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, session: SessionDependency):
    is_deleted = await BookRepository.delete_one(book_id, session)

    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга по ID {book_id} не найдена")

