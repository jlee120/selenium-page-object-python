from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def go_to(self, url):
        self.driver.get(url)

    def find_element(self, loc):
        return self.driver.find_element(loc)

    def get_page_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def wait_for_element_to_be_visible(self, loc):
        return self.wait.until(ec.visibility_of_element_located(loc))

    def wait_for_element_to_be_invisible(self, loc):
        return self.wait.until(ec.invisibility_of_element_located(loc))

    def wait_for_element_to_be_clickable(self, loc):
        return self.wait.until(ec.element_to_be_clickable(loc))

    def enter_text(self, loc, text):
        self.wait_for_element_to_be_visible(loc).send_keys(text)

    def click(self, loc):
        self.wait_for_element_to_be_clickable(loc).click()

    # Scrolling
    def scroll_element_into_view(self, by_loc):
        ele = self.find_element(by_loc)
        self.driver.execute_script("return arguments[0].scrollIntoView();", ele)

    def scroll_to_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top_of_page(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
