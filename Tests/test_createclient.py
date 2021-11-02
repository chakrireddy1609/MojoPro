import time
from uuid import uuid4
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Tests.BaseTest import BaseTest


class Test_CreateClient(BaseTest):
    def test_createclient(self):
        log = self.getLogger()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Email']").send_keys("ripple@joveo.com")
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Password']").send_keys("ripple")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Add Client']").click()
        client_name = self.driver.find_element(By.XPATH, "//input[@data-placeholder='Client Name*']")
        log.info(client_name.text)
        client_name.send_keys("ClientAuto_"+str(uuid4()))
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Exported Name*']").send_keys("ExportedNameAuto_"+str(uuid4()))
        self.driver.find_element(By.XPATH, "//span[text()='Timezone*']").click()
        self.driver.find_element(By.XPATH, "//span[text()='(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi']").click()
        self.driver.find_element(By.XPATH, "//span[text()='ATS Name*']").click()
        self.driver.find_element(By.XPATH, "//span[text()='App Vault']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Frequency*']").click()
        self.driver.find_element(By.XPATH, "//span[text()=' 3 hours ']").click()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Enter URL*']").send_keys("https://job-feeds-devlocal.s3.amazonaws.com/joveo-actual-10-jobs.xml")
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Map Feed']").click()
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Mandatory Fields']")))
        self.driver.find_element(By.XPATH, "//a[@class='unmap-field']").click()
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Monthly Budget*']").send_keys("10")
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Client End Date*']").click()
        self.driver.find_element(By.XPATH, "//div[text()=' 30 ']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Country/Region*']").click()
        self.driver.find_element(By.XPATH, "//span[text()='India']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Submit']").click()
        client_names = self.driver.find_elements(By.XPATH, "//a[contains(@class,'entity-tree__item-link')]")
        log.info(len(client_names))
        list_clients = []
        for name in client_names:
            name_text = name.text
            name_refined = name_text.replace("\nkeyboard_arrow_right","")
            list_clients.append(name_refined)
            continue
        assert [x for x in list_clients if 'ClientAuto_' in x]








