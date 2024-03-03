from base_page import BasePage
from page_elements import Input, Button


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username = Input(self.page,
                              selector="//input[@id='userName']",
                              name='UserName')
        self.password = Input(self.page, selector="//input[@id='password']", name='Password')
        self.login = Button(self.page, selector="//button[@id='login']", name='Login')
