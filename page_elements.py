import allure
from playwright.async_api import Page

from abc import abstractmethod, ABC


class PageElement(ABC):
    def __init__(self, page: Page, selector: str, name: str):
        self.page = page
        self.selector = selector
        self.name = name

    @property
    @abstractmethod
    def _type_of(self) -> str:
        return 'component'

    def _format_selector(self, **kwargs):
        return self.selector.format(**kwargs)

    def _format_name(self, **kwargs):
        return self.name.format(**kwargs)

    def click(self, **kwargs):
        with allure.step(f'Нажать {self._type_of}: "{self._format_name(**kwargs)}".'):
            self.page.click(self.selector)


class Button(PageElement):

    @property
    def _type_of(self):
        return 'Button'

    def dblclick(self, **kwargs):
        with allure.step(f'Нажать два раза {self._type_of}: "{self._format_name(**kwargs)}".'):
            self.page.dblclick(self.selector)


class Input(PageElement):

    @property
    def _type_of(self):
        return 'Input'

    def fill(self, text, **kwargs):
        with allure.step(f'Заполнить {self._type_of}: "{self._format_name(**kwargs)}".{text}'):
            self.page.fill(self.selector, value=text)


class Text(PageElement):

    @property
    def _type_of(self):
        return 'Text'
