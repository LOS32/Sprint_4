from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_title', [
        'Гордость и предубеждение и зомби',
        'Гордость и предубеждение и зомби.',
    ])
    def test_add_new_book_with_various_lengths(self, collector, book_title):
        collector.add_new_book(book_title)
        assert book_title in collector.get_books_genre()

    # Параметризуем тест для невалидных значений (41 символ и более)
    @pytest.mark.parametrize('book_title', [
        'Гордость и предубеждение и зомби Г',  # 41 символ
    ])
    def test_add_new_book_invalid_length(self, collector, book_title):
        collector.add_new_book(book_title)
        assert book_title not in collector.get_books_genre()

    def test_add_new_book_book_not_added_again(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_for_already_added_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_not_set_if_book_not_in_dictionary(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби']
        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_returns_correct_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_books_for_children()

    def test_add_book_in_favorites_if_book_in_dictionary(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби',
                                                           'Что делать, если ваш кот хочет вас убить']
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == []



















