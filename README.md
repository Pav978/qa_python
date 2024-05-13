Реализованно 12 тестов.
Из них 9 позитивных:

1. (PASSSED) test_add_new_book - добавление новой книги
2. (PASSSED) test_set_book_genre - установление жанра книги, если книга есть в books_genre ее жанр входит в список genre
3. (PASSSED) test_get_book_genre - вывод жанра книги по ее имени
4. (PASSSED) test_get_books_with_specific_genre - вывод списка книг с определенным жанром
5. (PASSSED) test_get_books_genre - вывод текущего словаря books_genre
6. (PASSSED) test_get_books_for_children - возврат книг, которые подходят детям.
7. (PASSSED) test_add_book_in_favorites - добавление книги в список избранных
8. (PASSSED) test_delete_book_from_favorites - удаление книги из списка избранных
9. (PASSSED) test_get_list_of_favorites_books - вывод списка избранных книг

Из них 3 негативных:
1. (PASSSED) test_add_new_book_with_empty_name - добавление пустого ввод в названии книги
2. (PASSSED) test_add_new_book_with_long_name - добавление книги с название более 41 символа
3. (FAILED) test_set_book_genre_with_incorrect_genre -  установление не существующего жанра для книги
