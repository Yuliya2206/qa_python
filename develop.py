import pytest
from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_existing_name(self):
        collector = BooksCollector()
        collector.add_new_book("Приключения Шерлока Холмса")
        collector.add_new_book("Приключения Шерлока Холмса")
        assert collector.get_books_genre() == {'Приключения Шерлока Холмса': ''}

    @pytest.mark.parametrize('name', ['Король Лев', 'Гарри Поттер', 'Преступление и наказание'])
    def test_add_new_book_with_valid_name(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()

    def test_set_book_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        assert collector.get_books_genre() == {'Преступление и наказание': 'Детективы'}

    def test_set_book_genre_for_notexisting_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_books_genre() == {}

    def test_set_book_genre_for_notexisting_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Фэнтези')
        assert collector.get_books_genre() == {'Преступление и наказание': ''}

    @pytest.mark.parametrize('name, genre', [('Король Лев', 'Мультфильмы'),
                                             ('Приключения Шерлока Холмса', 'Детективы')])
    def test_get_books_genre_get_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [('Король Лев', 'Мультфильмы'), ('Приключения Шерлока Холмса', 'Детективы')])
    def test_get_books_with_specific_genre_get_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_with_specific_genre_not_valid_genre(self, my_books_collection):
        assert len(my_books_collection.get_books_with_specific_genre('Фэнтези')) == 0

    def test_get_books_for_children(self, my_books_collection):
        assert len(my_books_collection.get_books_for_children()) == 3 and my_books_collection.get_books_for_children() == ['Шрэк', 'Гарри Поттер', 'Король Лев']
    def test_add_book_in_favorites_add_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Король Лев')
        assert 'Король Лев' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_again_in_favotites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Король Лев')
        my_books_collection.add_book_in_favorites('Король Лев')
        assert 'Король Лев' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_not_valid_dict_book(self, my_books_collection):
        book = 'Братья Карамазовы'
        my_books_collection.add_book_in_favorites(book)
        assert len(my_books_collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Король Лев')
        my_books_collection.delete_book_from_favorites('Король Лев')
        assert len(my_books_collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_deleted_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Король Лев')
        my_books_collection.delete_book_from_favorites('Гарри Поттер')
        assert len(my_books_collection.get_list_of_favorites_books()) == 1 and 'Гарри Поттер' not in my_books_collection.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Король Лев')
        my_books_collection.add_book_in_favorites('Шрэк')
        assert my_books_collection.get_list_of_favorites_books() == ['Король Лев', 'Шрэк']

