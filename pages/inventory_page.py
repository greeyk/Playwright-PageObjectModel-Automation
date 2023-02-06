from playwright.sync_api import Page

class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self._cart = page.locator("#shopping_cart_container a")
        self._add_backpack_btn = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self._remove_backpack_btn = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self._menu = page.get_by_role("button", name="Open Menu")
        self._logout = page.get_by_role("link", name="Logout")
        self._cart_icon = page.locator("#shopping_cart_container a")

    def load(self) -> None:
        self.page.goto(self.URL)

    def add_item(self) -> None:
        self._add_backpack_btn.click()

    def remove_item(self) -> None:
        self._remove_backpack_btn.click()

    def logout(self) -> None:
        self._menu.click()
        self._logout.click()

    def cart_icon_click(self) -> None:
        self._cart_icon.click()