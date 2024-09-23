import pytest
from main import BooksCollector


@pytest.fixture
def books_collection():
    books_collection = BooksCollector()
    return books_collection

@pytest.fixture
def my_books_collection(books_collection):
    my_collection = books_collection
    books = ['Шрэк', 'Приключения Шерлока Холмса', 'Преступление и наказание', 'Гарри Поттер', 'Король Лев']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(5):
        my_collection.add_new_book(books[i])
    for i in range(5):
        my_collection.set_book_genre(books[i], genre[i])
    return my_collection