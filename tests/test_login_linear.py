import time

from selenium import webdriver
import unittest, os
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):

    def setUp(self):
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        chrome_path = os.path.join(project_path, 'drivers/chromedriver')
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

        self.driver.find_element(By.ID, 'txtUsername').send_keys('admin')
        self.driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        self.driver.find_element(By.ID, 'btnLogin').click()
        welcome_text = self.driver.find_element(By.ID, 'welcome').text
        self.assertEqual(welcome_text, 'Welcome Admin')
        print("Login success!")
        self.driver.find_element(By.ID, 'welcome').click()
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as ec
        wait = WebDriverWait(self.driver, 3)
        wait.until(ec.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
