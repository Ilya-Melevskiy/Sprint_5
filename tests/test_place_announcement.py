from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from faker import Faker

from locators import Registration
from locators import Main
from locators import PlaceAnnouncement
from locators import PersonalАccount


class TestPlaceAnnouncement:
    
    def test_unauth_user_place_announcement(self, driver):
        driver.find_element(*Main.BUTTON_PLACE_ANNOUNCEMENT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PlaceAnnouncement.HEADER_MODAL_WINDOW_WITHOUT_LOGIN
            )
        )

        assert (
            driver.find_element(
                *PlaceAnnouncement.HEADER_MODAL_WINDOW_WITHOUT_LOGIN
            ).text
            == "Чтобы разместить объявление, авторизуйтесь"
        )

    def test_auth_user_place_announcement(self, driver):
        # Вызываю регистрацию вместо авторизации, потому что при создании более 3-х объявлений
        # для одного пользователя, новые объявления начинают уходить на следующую страницу
        driver.find_element(*Main.BUTTON_LOGIN_REGISTRATION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Registration.BUTTON_NO_ACCOUNT)
        )
        driver.find_element(*Registration.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                Registration.BUTTON_CREATE_ACCOUNT
            )
        )
        fake = Faker()
        driver.find_element(*Registration.INPUT_REGISTRATION_EMAIL).send_keys(
            fake.email()
        )
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

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Main.BUTTON_LOGOUT)
        )
        driver.find_element(*Main.BUTTON_PLACE_ANNOUNCEMENT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                PlaceAnnouncement.BUTTON_PUBLISH
            )
        )
        random_name = f"Тест{random.randint(0, 10000)}"
        driver.find_element(*PlaceAnnouncement.INPUT_NAME).send_keys(random_name)
        driver.find_element(*PlaceAnnouncement.TEXTAREA_DESCRIPTION).send_keys(
            "Тестовое описание"
        )
        driver.find_element(*PlaceAnnouncement.INPUT_PRICE).send_keys("500")
        driver.find_element(*PlaceAnnouncement.BUTTON_DROPDOWN_CATEGORY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                PlaceAnnouncement.CATEGORY_BOOKS
            )
        )
        driver.find_element(*PlaceAnnouncement.CATEGORY_BOOKS).click()
        driver.find_element(*PlaceAnnouncement.BUTTON_DROPDOWN_CITY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                PlaceAnnouncement.CITY_ST_PETERSBURG
            )
        )
        driver.find_element(*PlaceAnnouncement.CITY_ST_PETERSBURG).click()
        driver.find_element(*PlaceAnnouncement.RADIOBUTTON_BU).click()
        driver.find_element(*PlaceAnnouncement.BUTTON_PUBLISH).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Main.PAGINATION)
        )
        element = driver.find_element(*Main.BUTTON_AVATAR)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*Main.BUTTON_AVATAR).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PersonalАccount.HEADER_MY_ANNOUNCEMENT
            )
        )
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                PersonalАccount.NAME_LAST_ANNOUNCEMENT
            )
        )
        assert (
            driver.find_element(*PersonalАccount.NAME_LAST_ANNOUNCEMENT).text
            == random_name
        )
