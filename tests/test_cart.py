from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage

# login data
valid_username = "standard_user"
valid_password = "secret_sauce"


def test_cart_page_load(page: Page, login_page: LoginPage, cart_page: CartPage):
    cart_page.load()

    expect(login_page.error_msg) \
        .to_have_text("Epic sadface: You can only access '/cart.html' when you are logged in.")

    inventory_page = login_page.do_valid_login(valid_username, valid_password)
    inventory_page.cart_icon_click()

    assert page.url == "https://www.saucedemo.com/cart.html"


def test_item_in_cart(page: Page, login_page: LoginPage):
    login_page.load()
    inventory_page = login_page.do_valid_login(valid_username, valid_password)
    inventory_page.add_item()
    cart_page = inventory_page.cart_icon_click()

    assert cart_page.remove_btn.inner_text() == "REMOVE"


def test_remove_item_from_cart(page: Page, login_page: LoginPage):
    login_page.load()
    inventory_page = login_page.do_valid_login(valid_username, valid_password)
    inventory_page.add_item()
    cart_page = inventory_page.cart_icon_click()
    cart_page.remove_btn.click()

    # cart_page.remove_btn.to_have_count(0):

    # assert page.locator("#cart_contents_container").filter(has_text="removed")
    # expect(page.locator("#cart_contents_container").filter(has_text="removed"))
    print(str(page.locator('//*[@id="cart_contents_container"]/div/div[1]').get_attribute("removed_cart_item")))
