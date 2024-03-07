import allure
import pytest

from data_test.books_data import BooksData
from data_test.user_data import UserData


@pytest.mark.regress
@pytest.mark.profile
class TestProfile:
    @allure.title('Отображение NickName пользователя')
    def test_nickname_user(self, profile_page):
        # Act
        profile_page.auth(user=UserData.user1).open_page()

        # Assert
        profile_page.username.assert_text_eql(text=UserData.user1.userName)

    @allure.title(f'Отображение книги {BooksData.book1.title} в списке')
    def test_mock_book(self, profile_page):
        # Arrange
        book = BooksData.book1
        mock_response = {"books": [book.dict()]}

        # Act
        profile_page.mock(
            endpoint='**/BookStore/v1/Books',
            mock_response=mock_response
        )
        profile_page.auth(user=UserData.user1).open_page('books')

        # Assert
        profile_page.assert_book_in_table(book=book)
