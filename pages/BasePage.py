import conftest
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        self.searchBox = (By.XPATH, '//*[@id="root"]/div/div/main/div[2]/form/div[1]/div/div[1]/input')

    def search(self, text):
        self.driver.find_element(*self.searchBox).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()
