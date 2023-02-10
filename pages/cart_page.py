from playwright.sync_api import Page

class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.remove_btn = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

    def load(self):
        self.page.goto(self.URL)gita