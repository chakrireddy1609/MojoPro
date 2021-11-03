
import time
from uuid import uuid4

from selenium.webdriver.common.by import By

from Tests.BaseTest import BaseTest
from Utils import TestData


class Test_CreateJG(BaseTest):
    def test_createjg(self):
        log = self.getLogger()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Email']").send_keys(TestData.username)
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Password']").send_keys(TestData.password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@data-id='6b5e22dd-e32a-405f-b775-f0fdf54af547']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()=' Job Groups ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Add Job Group']").click()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Job Group Name*']").send_keys("JGAuto_" + str(uuid4()))
        self.driver.find_element(By.XPATH, "//span[text()='Campaign Name*']").click()
        self.driver.find_element(By.XPATH, "//span[text()=' Default Campaign ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Job Group End Date*']").click()
        self.driver.find_element(By.XPATH, "//div[text()=' 30 ']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Category']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()=' Requisition Id ']").click()
        self.driver.find_element(By.XPATH, "//span[text()='in']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()=' equal ']").click()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Enter Value']").send_keys("5")
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='cpcBid']").send_keys("1")
        self.driver.find_element(By.XPATH, "//input[@name='cpaBid']").send_keys("10")
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Target']").send_keys("5")
        self.driver.find_element(By.XPATH, "//div[text()=' APEC EURO ']/parent::td/parent::tr/td[1]/div").click()
        self.driver.find_element(By.XPATH, "//span[text()=' Submit ']").click()




