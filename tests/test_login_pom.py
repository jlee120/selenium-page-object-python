from selenium import webdriver
import unittest, os
from pages.login_page import LoginPage
from pages.home_page import HomePage


class LoginTest(unittest.TestCase):

    def setUp(self):
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        chrome_path = os.path.join(project_path, 'drivers/chromedriver')
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.maximize_window()

    def test_login_as_admin(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        # Login as admin
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'admin123')

        # Verify user has successfully logged in
        home_page = HomePage(self.driver)
        welcome_text = home_page.get_welcome_text()
        self.assertEqual(welcome_text, 'Welcome Admin')
        print("Login success!")

        # Log out
        home_page.logout()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
