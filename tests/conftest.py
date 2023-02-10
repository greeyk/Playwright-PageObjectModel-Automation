import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)