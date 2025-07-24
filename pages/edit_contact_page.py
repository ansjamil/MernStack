# edit_contact_page.py
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EditContactPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email']")
    UPDATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Update')]")
    BACK_BUTTON = (By.XPATH, "(//button[@class='btn3'])[1]")

    def update_contact(self, name, email):
        self.clear_and_type(*self.NAME_INPUT, name)
        self.clear_and_type(*self.EMAIL_INPUT, email)
        self.driver.find_element(*self.UPDATE_BUTTON).click()
        self.click_back_button(*self.BACK_BUTTON)
