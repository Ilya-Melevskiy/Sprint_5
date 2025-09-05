from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker

from locators import Registration
from locators import Main


def test_registration_user_success(driver):
    driver.find_element(*Main.BUTTON_LOGIN_REGISTRATION).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.BUTTON_NO_ACCOUNT)
    )
    driver.find_element(*Registration.BUTTON_NO_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.BUTTON_CREATE_ACCOUNT)
    )
    fake = Faker()
    driver.find_element(*Registration.INPUT_REGISTRATION_EMAIL).send_keys(fake.email())
    driver.find_element(*Registration.INPUT_REGISTRATION_PASSWORD).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.INPUT_REGISTRATION_REPEAT_PASSWORD).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.BUTTON_CREATE_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Main.BUTTON_AVATAR)
    )

    assert (
        driver.find_element(*Main.BUTTON_AVATAR)
        and driver.find_element(*Main.PROFILE_NAME).text == "User."
    )


def test_registration_user_invalid_email_error(driver):
    driver.find_element(*Main.BUTTON_LOGIN_REGISTRATION).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.BUTTON_NO_ACCOUNT)
    )
    driver.find_element(*Registration.BUTTON_NO_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.BUTTON_CREATE_ACCOUNT)
    )
    fake = Faker()
    invalid_email = fake.email().replace("@", "")
    driver.find_element(*Registration.INPUT_REGISTRATION_EMAIL).send_keys(invalid_email)
    driver.find_element(*Registration.BUTTON_CREATE_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Registration.ERROR_EMAIL)
    )

    assert (
        driver.find_element(*Registration.FIELD_REGISTRATION_EMAIL_ERROR)
        and driver.find_element(*Registration.FIELD_REGISTRATION_PASSWORD_ERROR)
        and driver.find_element(*Registration.FIELD_REGISTRATION_REPEAT_PASSWORD_ERROR)
        and driver.find_element(*Registration.ERROR_EMAIL)
    )


def test_registration_existing_user__error(driver):
    driver.find_element(*Main.BUTTON_LOGIN_REGISTRATION).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.BUTTON_NO_ACCOUNT)
    )
    driver.find_element(*Registration.BUTTON_NO_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.BUTTON_CREATE_ACCOUNT)
    )
    driver.find_element(*Registration.INPUT_REGISTRATION_EMAIL).send_keys(
        "test1235@mail.ru"
    )
    driver.find_element(*Registration.INPUT_REGISTRATION_PASSWORD).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.INPUT_REGISTRATION_REPEAT_PASSWORD).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.BUTTON_CREATE_ACCOUNT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Registration.ERROR_EMAIL)
    )

    assert (
        driver.find_element(*Registration.FIELD_REGISTRATION_EMAIL_ERROR)
        and driver.find_element(*Registration.FIELD_REGISTRATION_PASSWORD_ERROR)
        and driver.find_element(*Registration.FIELD_REGISTRATION_REPEAT_PASSWORD_ERROR)
        and driver.find_element(*Registration.ERROR_EMAIL)
    )
