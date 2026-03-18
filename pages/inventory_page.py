from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    FIRST_ITEM_ADD = (By.XPATH, "//button[contains(@id,'add-to-cart')]")
    CART_ICON     = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_product(self):
        self.click(self.FIRST_ITEM_ADD)

    def open_cart(self):
        self.click(self.CART_ICON)