import time

import allure
import pytest

from data_test.user_data import UserData

@pytest.mark.profile
class TestProfile:
    @allure.title('Visibility username in profile')
    def test_nickname_user(self, profile_page):
        # Act
        profile_page.auth(user=UserData.user1).open_page()
        profile_page.log_out.click()

        # Assert

