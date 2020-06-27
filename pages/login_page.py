from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textfield = (By.ID, 'txtUsername')
        self.password_text_field = (By.ID, 'txtPassword')
        self.login_button = (By.ID, 'btnLogin')

    def enter_username(self, username):
        self.driver.find_element(self.username_textfield, username)

    def enter_password(self, password):
        self.driver.find_element(self.password_text_field, password)

    def click_login(self):
        self.driver.find_element(self.login_button).click()

    def login_as_admin(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()