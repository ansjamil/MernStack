from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    ADD_CONTACT_BTN = (By.XPATH, "//button[contains(text(),'Add contact')]")

    def click_add_contact(self):
        self.click(self.ADD_CONTACT_BTN)
