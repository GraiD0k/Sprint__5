from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.urls import Urls
from helpers.locators import Locators
from conftest import driver



class TestRegistration:
    def test_registration_success(self,driver):
        driver.get(Urls.URL_BASE)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        driver.find_element(*Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.LINK_FOR_REGISTRATION_ON_LOGIN_PAGE)))
        driver.find_element(*Locators.LINK_FOR_REGISTRATION_ON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_REGISTRATION)))
        driver.find_element(*Locators.NAME_FOR_REGISTRATION).send_keys('Алёша')
        driver.find_element(*Locators.EMAIL_FOR_REGISTRATION).send_keys('AlekseyAlekseev_172634@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys('1112113')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        assert driver.current_url == Urls.URL_LOGIN

    def test_registration_incorrect_password(self, driver):
        driver.get(Urls.URL_REGISTRATION)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_REGISTRATION)))
        driver.find_element(*Locators.NAME_FOR_REGISTRATION).send_keys('Алёша_12_0123')
        driver.find_element(*Locators.EMAIL_FOR_REGISTRATION).send_keys('AlekseyAlekseev_172124@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys('112')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ERROR_FOR_INCORRECT_PASSWORD)))
        assert driver.find_element(*Locators.ERROR_FOR_INCORRECT_PASSWORD).text == 'Некорректный пароль'