from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, by, value):
        return self.driver.find_element(by, value).text

    def click_back_button(self, by, locator):
        self.driver.find_element(by, locator).click()

    def clear_and_type(self, by, locator, value):
        element = self.driver.find_element(by, locator)
        element.clear()
        element.send_keys(value)


