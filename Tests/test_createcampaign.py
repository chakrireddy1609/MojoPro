import time
from uuid import uuid4

from selenium.webdriver.common.by import By

from Tests.BaseTest import BaseTest
from Utils import TestData


class Test_CreateCampaign(BaseTest):
    def test_createcampaign(self):
        log = self.getLogger()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Email']").send_keys(TestData.username)
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Password']").send_keys(TestData.password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@data-id='6b5e22dd-e32a-405f-b775-f0fdf54af547']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Add Campaign']").click()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Campaign Name*']").send_keys("CampaignAuto_" + str(uuid4()))
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Budget']").send_keys("5")
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Campaign End Date*']").click()
        self.driver.find_element(By.XPATH, "//div[text()=' 30 ']").click()





