import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get('https://recrutement.natixis.com/en')
    if driver.find_element(By.ID, 'tarteaucitronAlertBigContent').is_displayed():
        driver.find_element(By.XPATH, '//*[@id="tarteaucitronPersonalize"]').click()
        driver.implicitly_wait(15)
    else:
        pass

    yield

    driver.quit()
