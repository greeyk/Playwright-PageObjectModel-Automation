from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# login data
valid_username = "standard_user"
valid_password = "secret_sauce"


def test_inventory_page_load(page: Page, inventory_page: InventoryPage, login_page: LoginPage) -> None:
    inventory_page.load()

    expect(login_page.error_msg)\
        .to_have_text("Epic sadface: You can only access '/inventory.html' when you are logged in.")

    login_page.do_login(valid_username, valid_password)

    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_add_item(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    inventory_page = login_page.do_valid_login(valid_username, valid_password)

    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_have_text("Add to cart")

    inventory_page.add_item()

    assert page.locator("#shopping_cart_container a").inner_text() == "1"

def test_remove_item(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    inventory_page = login_page.do_valid_login(valid_username, valid_password)
    inventory_page.add_item()

    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_have_text("Remove")

    inventory_page.remove_item()

    assert page.locator("#shopping_cart_container a").inner_text() == ""