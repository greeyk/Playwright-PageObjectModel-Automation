from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# login data
valid_username = "standard_user"
valid_password = "secret_sauce"
locked_username = "locked_out_user"
invalid_password = "wrong_password"


def test_login_with_valid_user(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    expect(page).to_have_url("https://www.saucedemo.com/")

    login_page.do_valid_login(valid_username, valid_password)

    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_login_with_invalid_user(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    login_page.do_login(valid_username, invalid_password)

    assert login_page.error_msg.inner_text() ==\
           "Epic sadface: Username and password do not match any user in this service"

def test_login_with_locked_user(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    login_page.do_login(locked_username, valid_password)

    assert login_page.error_msg.inner_text() == "Epic sadface: Sorry, this user has been locked out."

def test_login_without_username(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    login_page.do_login('', valid_password)

    assert login_page.error_msg.inner_text() == "Epic sadface: Username is required"

def test_login_without_password(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    login_page.do_login(valid_username, '')

    assert login_page.error_msg.inner_text() == "Epic sadface: Password is required"

def test_logout(page: Page, login_page: LoginPage) -> None:
    login_page.load()
    inventory_page = login_page.do_valid_login(valid_username, valid_password)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    inventory_page.logout()

    assert page.url == "https://www.saucedemo.com/"

