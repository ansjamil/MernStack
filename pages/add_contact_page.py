from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddContactPage(BasePage):
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBMIT_BTN = (By.XPATH, "//button[contains(text(),'Add')]")
    BACK_BUTTON = (By.XPATH, "(//button[@class='btn3'])[1]")

    def add_contact(self, name, email):
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BTN)


        self.click_back_button(*self.BACK_BUTTON)