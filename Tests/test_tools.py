import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Tests.BaseTest import BaseTest
from Utils import TestData


class Test_Tools(BaseTest):
    def test_tools(self):
        log = self.getLogger()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Email']").send_keys(TestData.username)
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Password']").send_keys(TestData.password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Conversion Tracking']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Client Name']")))
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Publisher Feeds']").click()
        time.sleep(1)
        count_of_feeds = self.driver.find_elements(By.XPATH, "//span[@class='feedURL']")
        assert len(count_of_feeds) != 0
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Reports']").click()
        time.sleep(1)
        count_of_td = "//div[@class='m-cell-data ng-star-inserted']"
        assert len(count_of_td) != 0
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Manage Tags']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Select Client']")))
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Markups']").click()
        time.sleep(1)
        count_of_td_markup = self.driver.find_elements(By.XPATH, "//div[@class='m-cell-data ng-star-inserted']")
        assert len(count_of_td_markup) != 0
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Publisher Management']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Publishers']")))
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='CD User Management']").click()
        time.sleep(1)
        clients_displayed_cd = self.driver.find_elements(By.XPATH, "//span[@class='mx-l-2 ng-star-inserted']")
        assert len(clients_displayed_cd) != 0
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Scheduler Tasks']").click()
        time.sleep(1)
        clients_displayed_schedulertasks = self.driver.find_elements(By.XPATH, "//td[@class='ng-star-inserted']")
        assert len(clients_displayed_schedulertasks) != 0
        self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='build']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()







