import allure
from playwright.sync_api import sync_playwright, Page

from fixtures.account_fixtures import *

from data_test.user_data import UserData
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from singleton import BaseUrlSingleton

import os

from utils.api.account_api import AccountApi
from utils.api.api_facade import ApiFacade


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help='Браузер для запуска тестов')
    parser.addoption('--headless', action='store_true', default=None,
                     help='Запуск браузера без окна')
    parser.addoption('--base_url', action='store', default=os.getenv("HOST", "https://demoqa.com/"),
                     help='Выберите хост, для работы тестов')


@pytest.fixture(scope='session')
def chromium_page(api_clients) -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=True)
        yield chromium.new_page()
        chromium.close()


@pytest.fixture(scope="function")
def profile_page(chromium_page):
    return ProfilePage(chromium_page)


@pytest.fixture(scope="function")
def login_page(chromium_page):
    return LoginPage(chromium_page)


@pytest.fixture(scope="session", autouse=True)
def setup_base_url(request):
    base_url = request.config.getoption("--base_url")
    BaseUrlSingleton.set_base_url(base_url)


@pytest.fixture(scope='session')
def api_clients():
    user_clients = {}

    for user in [UserData.user1, UserData.user2]:
        user.userId = AccountApi(module='Account').create_user(user)['userID']
        user.token = AccountApi(module='Account').generate_token(user=user)['token']
        api_client_instance = ApiFacade(auth_token=user.token)

        user_clients[user.userId] = api_client_instance

    yield user_clients

    for user in [UserData.user1, UserData.user2]:
        user_clients[user.userId].account.delete_user(user)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("chromium_page")
        if page:
            try:
                screenshot = page.screenshot(full_page=True)
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")


