from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


class LoginPage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self._login_button = page.locator("[data-test=\"login-button\"]")
        self._username_input = page.locator("[data-test=\"username\"]")
        self._password_input = page.locator("[data-test=\"password\"]")
        self._error_message = page.locator("[data-test=\"error\"]")

    def load(self) -> None:
        self.page.goto(self.URL)

    def do_login(self, username: str, password: str):
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()

    def do_valid_login(self, username: str, password: str):
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()
        return InventoryPage(self.page)

    @property
    def error_msg(self):
        return self._error_message