from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        self.searchBox = (By.XPATH, '//*[@id="root"]/div/div/main/div[2]/form/div[1]/div/div[1]/input')

    def search(self, text):
        self.driver.find_element(*self.searchBox).send_keys(text)

    def click(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable((by, value))
            )
            element.click()
        except TimeoutException:
            print(f"Element {by}='{value}' was not clickable within {timeout} seconds.")
