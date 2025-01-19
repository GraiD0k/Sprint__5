from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls
from conftest import driver


class TestPersonalAccount:
    def test_go_click_to_personal_account(self, driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_FOR_PAGE_LOGIN))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('AlekseyAlekseev_172634@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('1112113')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_MAKE_ORDERS))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT ).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_PROFILE))
        assert driver.current_url == Urls.URL_PERSONAL_ACCOUNT

    def test_go_click_to_constructor(self,driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_FOR_PAGE_LOGIN))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('AlekseyAlekseev_172634@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('1112113')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_MAKE_ORDERS))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_PROFILE))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE))
        assert driver.current_url == Urls.URL_BASE

    def test_go_click_to_logo(self,driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('AlekseyAlekseev_172634@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('1112113')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_MAKE_ORDERS)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_PROFILE)))
        driver.find_element(*Locators.LOGO_PAGE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE))
        assert driver.current_url == Urls.URL_BASE