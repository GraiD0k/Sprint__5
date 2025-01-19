from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.urls import Urls
from conftest import driver

class TestLogout:
    def test_logout_from_personal_account(self, driver):
        driver.get(Urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.TITLE_FOR_PAGE_LOGIN)))
        driver.find_element(*Locators.NAME_FOR_LOGIN).send_keys('AlekseyAlekseev_1914@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FOR_LOGIN).send_keys('11122253')
        driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTORIZATION_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_MAKE_ORDERS)))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_PROFILE)))
        driver.find_element(*Locators.BUTTON_EXIT_FROM_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_FOR_PAGE_LOGIN))
        assert driver.current_url == Urls.URL_LOGIN