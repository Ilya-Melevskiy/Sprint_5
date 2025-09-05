from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Login
from locators import Main


def test_login_user_success(driver):
    driver.find_element(*Main.BUTTON_LOGIN_REGISTRATION).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Login.BUTTON_LOGIN)
    )
    driver.find_element(*Login.INPUT_EMAIL).send_keys("test1235@mail.ru")
    driver.find_element(*Login.INPUT_PASSWORD).send_keys("12345qwerty")
    driver.find_element(*Login.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Main.BUTTON_AVATAR)
    )

    assert (
        driver.find_element(*Main.BUTTON_AVATAR)
        and driver.find_element(*Main.PROFILE_NAME).text == "User."
    )