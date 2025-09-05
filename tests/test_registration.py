from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker

from locators import Registration
from locators import Main


def test_registration_user_success(driver):
    driver.find_element(*Main.button_login_registration).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.button_no_account)
    )
    driver.find_element(*Registration.button_no_account).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.button_create_account)
    )
    fake = Faker()
    driver.find_element(*Registration.input_registration_email).send_keys(fake.email())
    driver.find_element(*Registration.input_registration_password).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.input_registration_repeat_password).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.button_create_account).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Main.button_avatar)
    )

    assert (
        driver.find_element(*Main.button_avatar)
        and driver.find_element(*Main.profile_name).text == "User."
    )


def test_registration_user_invalid_email_error(driver):
    driver.find_element(*Main.button_login_registration).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.button_no_account)
    )
    driver.find_element(*Registration.button_no_account).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.button_create_account)
    )
    fake = Faker()
    invalid_email = fake.email().replace("@", "")
    driver.find_element(*Registration.input_registration_email).send_keys(invalid_email)
    driver.find_element(*Registration.button_create_account).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Registration.error_email)
    )

    assert (
        driver.find_element(*Registration.field_registration_email_error)
        and driver.find_element(*Registration.field_registration_password_error)
        and driver.find_element(*Registration.field_registration_repeat_password_error)
        and driver.find_element(*Registration.error_email)
    )


def test_registration_existing_user__error(driver):
    driver.find_element(*Main.button_login_registration).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.button_no_account)
    )
    driver.find_element(*Registration.button_no_account).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Registration.button_create_account)
    )
    driver.find_element(*Registration.input_registration_email).send_keys(
        "test1235@mail.ru"
    )
    driver.find_element(*Registration.input_registration_password).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.input_registration_repeat_password).send_keys(
        "12345qwerty"
    )
    driver.find_element(*Registration.button_create_account).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Registration.error_email)
    )

    assert (
        driver.find_element(*Registration.field_registration_email_error)
        and driver.find_element(*Registration.field_registration_password_error)
        and driver.find_element(*Registration.field_registration_repeat_password_error)
        and driver.find_element(*Registration.error_email)
    )
