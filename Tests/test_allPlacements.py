import time
from selenium.webdriver.common.by import By

from Tests.BaseTest import BaseTest
from Utils import TestData

class Test_AllPlacements(BaseTest):
    def test_allplacements(self):
        log = self.getLogger()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Email']").send_keys(TestData.username)
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Password']").send_keys(TestData.password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()=' All Publishers ']").click()
        time.sleep(3)
        count_of_placements = self.driver.find_elements(By.XPATH, "//div[@class='m-cell-data ng-star-inserted']/a")
        time.sleep(3)
        assert len(count_of_placements) != 0

