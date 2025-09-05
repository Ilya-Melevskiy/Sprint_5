from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Login
from locators import Main


def test_logout_user_success(driver):
    driver.find_element(*Main.button_login_registration).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Login.button_login)
    )
    driver.find_element(*Login.input_email).send_keys("test1235@mail.ru")
    driver.find_element(*Login.input_password).send_keys("12345qwerty")
    driver.find_element(*Login.button_login).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Main.button_logout)
    )
    driver.find_element(*Main.button_logout).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Main.button_login_registration)
    )

    assert driver.find_element(*Main.button_login_registration)
