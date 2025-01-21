from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.urls import Urls
from helpers.locators import Locators
from conftest import driver

class TestConstructorPage:
    def test_click_to_sauces_in_constructor(self,driver):
        driver.get(Urls.URL_BASE)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.LINK_BUNS_CONSTRUCTOR)))
        driver.find_element(*Locators.LINK_SAUCES_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.FIRST_SAUCE)))
        assert driver.find_element(*Locators.NEW_LINK_SAUCES_CONSTRUCTOR).is_displayed()

    def test_click_to_buns_in_constructor(self,driver):
        driver.get(Urls.URL_BASE)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.LINK_BUNS_CONSTRUCTOR)))
        driver.find_element(*Locators.LINK_SAUCES_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.FIRST_SAUCE)))
        driver.find_element(*Locators.LINK_BUNS_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.FIRST_BUNS)))
        assert driver.find_element(*Locators.NEW_LINK_BUNS_CONSTRUCTOR).is_displayed()

    def test_click_to_filling_in_constructor(self,driver):
        driver.get(Urls.URL_BASE)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.LINK_BUNS_CONSTRUCTOR)))
        driver.find_element(*Locators.LINK_FILLING_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.FIRST_FILLING)))
        assert driver.find_element(*Locators.NEW_LINK_FILLING_CONSTRUCTOR).is_displayed()