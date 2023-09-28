import pytest
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.job_offers
class TestExploringJobOffers:
    def test_exploring_job_offers(self):
        test = BasePage()
        test.click(By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div/div/p/a')
        test.search("QA")


