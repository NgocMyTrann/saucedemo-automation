from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRSTNAME = (By.ID, "first-name")
    LASTNAME  = (By.ID, "last-name")
    ZIPCODE   = (By.ID, "postal-code")
    CONTINUE  = (By.ID, "continue")
    FINISH    = (By.ID, "finish")

    def fill_info(self, fn, ln, zip):
        self.type(self.FIRSTNAME, fn)
        self.type(self.LASTNAME, ln)
        self.type(self.ZIPCODE, zip)
        self.click(self.CONTINUE)
        self.click(self.FINISH)