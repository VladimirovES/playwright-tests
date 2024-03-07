import allure
from playwright.async_api import Page

from pages.base_page import BasePage
from models.books import Book
from pages.components.input import Input
from pages.components.image import Image
from pages.components.text import Text
from pages.components.button import Button


class ProfilePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_page(self, route='profile'):
        super().open_page(route)

        self.log_out = Button(self._page,
                              locator="//button[@id='submit']",
                              name='Log out')

        self.username = Text(self._page,
                             locator="//*[@id='userName-value']",
                             name='username')
        self.delete_account = Button(self._page,
                                     locator="//*[@class='text-right button di']//button[@class='btn btn-primary']",
                                     name='Delete Account')
        self.input_search_book = Input(self._page,
                                       locator="//input[@id='searchBox']",
                                       name='Search Books')
        self.image_book = Image(self._page, locator="//div[@class='rt-tr-group']['{line}']//img",
                                name='Image book')
        self.title_book = Text(self._page,
                               locator="//div[@class='rt-tr-group']['{line}']//*[contains(@id, 'see-book-{title}')]",
                               name='Title book "{title}"')

        self.author_book = Text(self._page,
                                locator="//div[@class='rt-tr-group']['{line}']//div[text()='{author}']",
                                name='Author book "{author}"')
        self.publisher = Text(self._page,
                              locator="//div[@class='rt-tr-group']['{line}']//div[text()='{publisher}']",
                              name='Publisher "{publisher}"')

    def assert_book_in_table(self, book: Book, line=1):
        with allure.step(f'Book data is present in line № {line}'):
            self.image_book.assert_visibility(line=line)
            self.image_book.assert_visibility(line=line)
            self.title_book.assert_visibility(line=line, title=book.title)
            self.author_book.assert_visibility(line=line, author=book.author)
            self.publisher.assert_visibility(line=line, publisher=book.publisher)
