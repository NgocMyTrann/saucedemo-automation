from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR = (By.CLASS_NAME,"error-message-container")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self, error):
        return self.type(self.ERROR, error)