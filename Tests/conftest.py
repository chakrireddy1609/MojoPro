import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utils import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = Service(GeckoDriverManager.install())
        driver = webdriver.Firefox(service=service)
    driver.get(TestData.URL)
    request.cls.driver = driver
    yield
    driver.close()


# @pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # to remove environment section
    config._metadata = None

    if not os.path.exists('Reports'):
        os.makedirs('Reports')

    config.option.htmlpath = '/Users/chakri/PycharmProjects/MojoPro/Reports/' + "Report_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"