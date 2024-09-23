# qa_python
Цель: покрыть тестами приложение BooksCollector, которое позволяет установить жанр книги и добавить их в избранное. 

Реализованы фикстуры:
books_collection: возвращает объект класса BooksCollector
my_books_collection: возвращает словарь {книга: жанр}

Сценарии, покрытые тестами:
1. test_add_new_book_add_two_books: Проверка добавления двух книг
2. test_add_new_book_add_existing_name: Проверка повторного добавления книги(негативный)
3. test_add_new_book_with_valid_name: Проверка добавления книги с валидным названием
4. test_set_book_genre_for_existing_book: Проверка добавления жанра (genre) для существующей книги из book_genre
5. test_set_book_genre_for_notexisting_book: Проверка добавления жанра (genre) для несуществующей книги, не из book_genre (негативный)
6. test_set_book_genre_for_notexisting_genre: Проверка добавления несуществующего жанра (не из genre) для книги из book_genre (негатвный)
7. test_get_books_genre_get_by_name: Проверка вывода жанра книги по ее имени
8. test_get_books_with_specific_genre_get_by_genre: Проверка вывода книг по жанру
9. test_get_books_with_specific_genre_not_valid_genre: Проверка вывода книг по жанру не из genre (негативная)
10. test_get_books_for_children: Проверка вывода детских книг
11. test_add_book_in_favorites_add_in_favorites_book: Проверка добавления книги в избранное
12. test_add_book_in_favorites_add_again_in_favotites_book: Проверка повторного добавления кного в избранное (негативная)
13. test_add_book_in_favorites_not_valid_dict_book: Проверка добавления книги в избранное не из book_genre (негативная)
14. test_delete_book_from_favorites: Проверка удаления книги из избранного
15. test_delete_book_from_favorites_deleted_book: Проверка удаления книги из избранного, не добавленной в избранное (негативная)
16. test_get_list_of_favorites_books: Проверка получения списка книг из избранного
