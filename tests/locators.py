from selenium.webdriver.common.by import By



class Registration:

    BUTTON_NO_ACCOUNT = (By.XPATH, ".//button[@style='max-width: 166px;']")
    INPUT_REGISTRATION_EMAIL = (By.XPATH, ".//input[@class='input_inputStandart__JweLZ spanGlobal' and @name='email']")
    INPUT_REGISTRATION_PASSWORD = (By.XPATH, ".//input[@class='input_inputStandart__JweLZ spanGlobal' and @name='password']")
    INPUT_REGISTRATION_REPEAT_PASSWORD = (By.XPATH, ".//input[@class='input_inputStandart__JweLZ spanGlobal' and @name='submitPassword']")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, ".//button[@type='submit' and @style='max-width: 192px;']")
    FIELD_REGISTRATION_EMAIL_ERROR = (By.XPATH, ".//div[@style='margin: 0px; max-width: 472px; width: 100%;']/div[@class='input_inputError__fLUP9']")
    FIELD_REGISTRATION_PASSWORD_ERROR = (By.XPATH, ".//input[@placeholder='Пароль']/parent::div[@class='input_inputError__fLUP9']")
    FIELD_REGISTRATION_REPEAT_PASSWORD_ERROR = (By.XPATH, ".//input[@placeholder='Повторите пароль']/parent::div[@class='input_inputError__fLUP9']")
    ERROR_EMAIL = (By.XPATH, ".//div[@style='margin: 0px; max-width: 472px; width: 100%;']/span[@class='input_span__yWPqB']")


class Login:

    INPUT_EMAIL = (By.XPATH, ".//input[@placeholder='Введите Email']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@placeholder='Пароль']")
    BUTTON_LOGIN = (By.XPATH, ".//button[@style='max-width: 111px;']")

class Main:

    BUTTON_LOGIN_REGISTRATION = (By.XPATH, ".//button[@style='max-width: 217px;']")
    BUTTON_AVATAR = (By.XPATH, ".//button[@class='circleSmall']")
    PROFILE_NAME = (By.XPATH, ".//h3[@class='profileText name']")
    BUTTON_PLACE_ANNOUNCEMENT = (By.XPATH, ".//button[@class='buttonPrimary inButtonText undefined inButtonText']")
    BUTTON_LOGOUT = (By.XPATH, ".//button[@class='spanGlobal btnSmall']")
    PAGINATION = (By.XPATH, ".//p[@class='spanGlobal']")

class PlaceAnnouncement:

    HEADER_MODAL_WINDOW_WITHOUT_LOGIN = (By.XPATH, ".//div[@class='popUp_titleRow__M7tGg']/h1")
    INPUT_NAME = (By.XPATH, ".//input[@placeholder='Название']")
    TEXTAREA_DESCRIPTION = (By.XPATH, ".//textarea[@placeholder='Описание товара']")
    INPUT_PRICE = (By.XPATH, ".//input[@placeholder='Стоимость']")
    BUTTON_DROPDOWN_CATEGORY = (By.XPATH, ".//div[@style='margin: 0px; max-width: 312px; width: 100%;']/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    CATEGORY_BOOKS = (By.XPATH, ".//span[text()='Книги']/parent::button")
    BUTTON_DROPDOWN_CITY = (By.XPATH, ".//div[@style='margin: 0px; max-width: 760px; width: 100%;']/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    CITY_ST_PETERSBURG = (By.XPATH, ".//span[text()='Санкт-Петербург']/parent::button")
    RADIOBUTTON_BU = (By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']") 
    BUTTON_PUBLISH = (By.XPATH, ".//button[text()='Опубликовать']")

class PersonalАccount:
    HEADER_MY_ANNOUNCEMENT = (By.XPATH, ".//h1[text()='Мои объявления']")
    NAME_LAST_ANNOUNCEMENT = (By.XPATH, ".//div[@class='card'][last()]//div[@class='about']//h2")