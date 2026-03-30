import time
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC
import pytest
from testdata.login_data import login_test_data
from selenium.webdriver.chrome.options import Options

@allure.feature("Purchase Flow")
@allure.story("User can buy product")
@allure.title("Verify user can complete purchase")

@pytest.mark.parametrize("username,password,expected", login_test_data)
def test_purchase_flow(login_page, inventory_page, cart_page, checkout_page, username, password, expected):

    with allure.step("Login with user"):
        login_page.login(username, password)

    if expected == "success":

        with allure.step("Add product to cart"):
            inventory_page.add_product_to_cart()

        with allure.step("Open cart"):
            cart_page.open_cart()

        with allure.step("Checkout product"):
            checkout_page.complete_checkout()

        assert checkout_page.is_order_successful()

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

    inventory = InventoryPage(driver)
    inventory.add_first_product()
    inventory.open_cart()
    print("Open Cart Passed")

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("My", "Tran", "70000")

    time.sleep(2)

    options = Options()
    options.add_experimental_option("detach", True)

    # Assertion – ví dụ xác nhận URL đã vào trang hoàn thành
    assert "checkout-complete" in driver.current_url

# driver.quit()