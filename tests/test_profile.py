import allure
import pytest

from data_test.books_data import BooksData
from data_test.user_data import UserData
from singleton import BaseUrlSingleton
from utils.routing import Routing


@pytest.mark.regress
@pytest.mark.profile
class TestProfile:
    @allure.title('Отображение NickName пользователя')
    def test_nickname_user(self, profile_page):
        # Act
        profile_page.auth(user=UserData.user1).open_page()

        # Assert
        profile_page.username.assert_text_eql(text=UserData.user1.userName)

    @allure.title('Logout')
    def test_logout_user(self, profile_page):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url() + f'{Routing.login}'

        # Act
        profile_page.auth(user=UserData.user2).open_page()
        profile_page.log_out.click()


        # Assert
        profile_page.assert_url_window_eql(expected_url)

    @allure.title(f'Отображение книги {BooksData.book1.title} в списке')
    def test_mock_book(self, profile_page):
        # Arrange
        book = BooksData.book1
        profile_page.mock(
            endpoint='**/BookStore/v1/Books',
            mock_response={"books": [book.dict()]}
        )

        # Act
        profile_page.auth(user=UserData.user1).open_page('books')

        # Assert
        profile_page.assert_book_in_table(book=book)
