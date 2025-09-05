from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from faker import Faker

from locators import Registration
from locators import Main
from locators import PlaceAnnouncement
from locators import PersonalАccount


def test_unauth_user_place_announcement(driver):
    driver.find_element(*Main.button_place_announcement).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            PlaceAnnouncement.header_modal_window_without_login
        )
    )

    assert (
        driver.find_element(*PlaceAnnouncement.header_modal_window_without_login).text
        == "Чтобы разместить объявление, авторизуйтесь"
    )


def test_auth_user_place_announcement(driver):
    # Вызываю регистрацию вместо авторизации, потому что при создании более 3-х объявлений
    # для одного пользователя, новые объявления начинают уходить на следующую страницу
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

    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Main.button_logout)
    )
    driver.find_element(*Main.button_place_announcement).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(PlaceAnnouncement.button_publish)
    )
    random_name = f"Тест{random.randint(0, 10000)}"
    driver.find_element(*PlaceAnnouncement.input_name).send_keys(random_name)
    driver.find_element(*PlaceAnnouncement.textarea_description).send_keys(
        "Тестовое описание"
    )
    driver.find_element(*PlaceAnnouncement.input_price).send_keys("500")
    driver.find_element(*PlaceAnnouncement.button_dropdown_category).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(PlaceAnnouncement.category_books)
    )
    driver.find_element(*PlaceAnnouncement.category_books).click()
    driver.find_element(*PlaceAnnouncement.button_dropdown_city).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(
            PlaceAnnouncement.city_st_petersburg
        )
    )
    driver.find_element(*PlaceAnnouncement.city_st_petersburg).click()
    driver.find_element(*PlaceAnnouncement.radiobutton_bu).click()
    driver.find_element(*PlaceAnnouncement.button_publish).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Main.pagination)
    )
    element = driver.find_element(*Main.button_avatar)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.find_element(*Main.button_avatar).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            PersonalАccount.header_my_announcement
        )
    )
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            PersonalАccount.name_last_announcement
        )
    )
    assert (
        driver.find_element(*PersonalАccount.name_last_announcement).text == random_name
    )
