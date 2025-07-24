import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")
    driver.maximize_window()
    yield driver
    driver.quit()
