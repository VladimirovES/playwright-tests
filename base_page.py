import allure

from singleton import BaseUrlSingleton


class BasePage:
    def __init__(self, page):
        self._page = page
        self.host = BaseUrlSingleton.get_base_url()

    def open_page(self, route: str = None):
        url = f"{self.host}{route}" if route else self.host
        self._page.goto(url)

    def auth(self, user):
        with allure.step(f"Добавить куки для пользователя: {user.userName}"):
            domain = self.host.split("//")[-1].split('/')[0]

            self._page.goto(self.host, wait_until='domcontentloaded')
            cookies = [
                {'name': 'token', 'value': user.token, 'domain': domain, 'path': '/'},
                {'name': 'userID', 'value': user.userId, 'domain': domain, 'path': '/'},
                {'name': 'userName', 'value': user.userName, 'domain': domain, 'path': '/'},
                {'name': 'expires', 'value': '2025-02-11T16:33:08.160Z', 'domain': domain, 'path': '/'},
            ]

            for cookie in cookies:
                self._page.context.add_cookies([cookie])

            return self

    def close_page(self):
        self._page.close()
    #
    # def auth_and_open_page(self, route, user):
    #     domain = self.host.split("//")[-1].split('/')[0]
    #     self._page.goto(self.host, wait_until="domcontentloaded")
    #
    #     cookies = [
    #         {'name': 'token', 'value': user.token, 'domain': domain, 'path': '/'},
    #         {'name': 'userID', 'value': user.userId, 'domain': domain, 'path': '/'},
    #         {'name': 'userName', 'value': user.userName, 'domain': domain, 'path': '/'},
    #         {'name': 'expires', 'value': '2025-02-11T16:33:08.160Z', 'domain': domain, 'path': '/'},
    #     ]
    #
    #     for cookie in cookies:
    #         self._page.context.add_cookies([cookie])
    #
    #     url = f"{self.host}{route}" if route else self.host
    #     self._page.goto(url)


