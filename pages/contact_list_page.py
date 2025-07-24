from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactListPage(BasePage):
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Search Contact"]')
    RESULT_TEXT = (By.XPATH, '(//div[contains(text(),"@")])[1]')
    EDIT_ICON = (By.XPATH, "(//i[@class='edit-icon fa fa-edit'])[1]")

    # Assumes email appears

    def search_contact(self, keyword):
        self.driver.find_element(*self.SEARCH_INPUT).clear()
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(keyword)

    def get_result_text(self):
        return self.get_text(*self.RESULT_TEXT)

    def click_edit_icon(self):
        self.driver.find_element(*self.EDIT_ICON).click()



