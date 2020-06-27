from selenium.webdriver.common.by import By
from locators.locators import Locators as loc
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_textfield = (By.ID, loc.username_textfield_id)
        self.password_textfield = (By.ID, loc.password_textfield_id)
        self.login_button = (By.ID, loc.login_button_id)

    def enter_username(self, username):
        super().enter_text(self.username_textfield, username)

    def enter_password(self, password):
        super().enter_text(self.password_textfield, password)

    def click_login(self):
        super().click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
