import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()