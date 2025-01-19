from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.urls import Urls
from helpers.locators import Locators
from conftest import driver


class TestAutorization:
    def test_log_in_on_main_page (self,driver):#вход по кнопке «Войти в аккаунт» на главной
        driver.get(Urls.URL_BASE)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        driver.find_element(*Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_LOGIN)))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('123@qw3234eq955.rge')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('1112225')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.URL_BASE

    def test_log_in_personal_account   (self, driver):    #вход через кнопку «Личный кабинет»
        driver.get(Urls.URL_BASE)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_LOGIN)))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('123@qw3234eq955.rge')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('1112225')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.URL_BASE

    def test_log_in_on_page_registration_form(self, driver):     #вход через кнопку в форме регистрации
        driver.get(Urls.URL_REGISTRATION)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_REGISTRATION)))
        driver.find_element(*Locators.LINK_LOGIN_ON_REGISTRATIONS_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_LOGIN)))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('123@qw3234eq955.rge')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('1112225')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.URL_BASE

    def test_log_in_on_page_forgot_password(self, driver):    #вход через кнопку в форме восстановления пароля.
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_LOGIN)))
        driver.find_element(*Locators.LINK_FORGOT_PASSWORD_ON_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.LINK_LOGIN_ON_REGISTRATIONS_PAGE)))
        driver.find_element(*Locators.LINK_LOGIN_ON_REGISTRATIONS_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.NAME_FOR_LOGIN)))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('123@qw3234eq955.rge')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('1112225')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE)))
        assert driver.current_url == Urls.URL_BASE