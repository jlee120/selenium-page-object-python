from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.welcome_link = (By.ID, 'welcome')
        self.logout_link = (By.LINK_TEXT, 'Logout')

    def get_welcome_text(self):
        return super().wait_for_element_to_be_visible(self.welcome_link).text

    def click_welcome_link(self):
        super().click(self.welcome_link)

    def click_logout_link(self):
        super().click(self.logout_link)

    def logout(self):
        self.click_welcome_link()
        self.click_logout_link()
