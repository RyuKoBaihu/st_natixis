import pytest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.job_offers
class TestExploringJobOffers:
    def test_exploring_job_offers(self):
        test = BasePage()
        test.click(By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div/div/p/a')
        ec.title_is("Our job offers - Natixis GFS")
        ec.url_changes("https://recrutement.natixis.com/en/our-job-offers?external=false")
        test.search("QA")
