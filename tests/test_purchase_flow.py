import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest
from testdata.login_data import login_test_data

@pytest.mark.parametrize("username,password,expected", login_test_data)
def test_login(driver, username, password, expected):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    if expected == "success":
        assert "inventory" in driver.current_url
    else:
        error = login_page.get_error_message()
        assert "error" in error.lower()

@allure.feature("Purchase Flow")
def test_purchase_flow(logged_in_driver):

    with allure.step("Add product"):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_first_product()

    with allure.step("Open cart"):
        inventory.open_cart()

    with allure.step("Checkout"):
        cart = CartPage(logged_in_driver)
        cart.checkout()

    with allure.step("Fill info"):
        checkout = CheckoutPage(logged_in_driver)
        checkout.fill_info("My", "Tran", "70000")

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return driver