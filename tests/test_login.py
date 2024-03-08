import allure
from qaseio.pytest import qase

from data_test.user_data import UserData
from singleton import BaseUrlSingleton
from utils.routing import Routing
import pytest


@pytest.mark.regress
@pytest.mark.login
@allure.epic('User')
@allure.feature('LoginPage')
@qase.suite(title='LoginPage')
class TestLogin:

    @allure.story('Invalid Login')
    @allure.title('With username "{login}" and password "{password}"')
    @qase.id(1)
    @qase.title('With username "{login}" and password "{password}"')
    @pytest.mark.parametrize('login, password', [(UserData.user_changes.userName, 'invalid'),
                                                 ('invalid_login', UserData.user_changes.password),
                                                 (UserData.user_changes.userName, ""),
                                                 ("", UserData.user_changes.password),
                                                 ("", ""),
                                                 ('invalid', 'invalid')])
    def test_invalid_login(self, login_page, login, password):
        # Act
        login_page.open_page()
        login_page.sign_in(login=login, password=password)

        # Assert
        login_page.validation_error.assert_text_eql('Invalid username or password!')

    @allure.story('Login')
    @allure.title('With valid creeds"')
    @qase.id(2)
    @qase.title('With valid creeds"')
    def test_valid_login(self, login_page, create_user_for_login):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url() + f'{Routing.profile}'
        user = create_user_for_login

        # Act
        login_page.open_page()
        login_page.sign_in(login=user.userName, password=user.password)

        # Assert
        login_page.assert_url_window_eql(expected_url)
