from pages.base_page import BasePage
from pages.components.input import Input
from pages.components.button import Button
from pages.components.text import Text


class LoginPage(BasePage):

    def open_page(self, route='login'):
        super().open_page(route)

    def __init__(self):
        super().__init__()

        self.username = Input(
            locator="//input[@id='userName']",
            name='UserName')
        self.password = Input(locator="//input[@id='password']", name='Password')
        self.login = Button(locator="//button[@id='login']", name='Login')
        self.validation_error = Text(locator="//p[@class='mb-1']",
                                     name='Invalid Login or Password')

    def sign_in(self, login, password):
        self.username.fill(text=login)
        self.password.fill(text=password)
        self.login.click()
