from selenium.webdriver.common.by import By



class Registration:

    button_no_account = (By.XPATH, ".//button[@style='max-width: 166px;']")
    input_registration_email = (By.XPATH, ".//input[@class='input_inputStandart__JweLZ spanGlobal' and @name='email']")
    input_registration_password = (By.XPATH, ".//input[@class='input_inputStandart__JweLZ spanGlobal' and @name='password']")
    input_registration_repeat_password = (By.XPATH, ".//input[@class='input_inputStandart__JweLZ spanGlobal' and @name='submitPassword']")
    button_create_account = (By.XPATH, ".//button[@type='submit' and @style='max-width: 192px;']")
    field_registration_email_error = (By.XPATH, ".//div[@style='margin: 0px; max-width: 472px; width: 100%;']/div[@class='input_inputError__fLUP9']")
    field_registration_password_error = (By.XPATH, ".//input[@placeholder='Пароль']/parent::div[@class='input_inputError__fLUP9']")
    field_registration_repeat_password_error = (By.XPATH, ".//input[@placeholder='Повторите пароль']/parent::div[@class='input_inputError__fLUP9']")
    error_email = (By.XPATH, ".//div[@style='margin: 0px; max-width: 472px; width: 100%;']/span[@class='input_span__yWPqB']")


class Login:

    input_email = (By.XPATH, ".//input[@placeholder='Введите Email']")
    input_password = (By.XPATH, ".//input[@placeholder='Пароль']")
    button_login = (By.XPATH, ".//button[@style='max-width: 111px;']")

class Main:

    button_login_registration = (By.XPATH, ".//button[@style='max-width: 217px;']")
    button_avatar = (By.XPATH, ".//button[@class='circleSmall']")
    profile_name = (By.XPATH, ".//h3[@class='profileText name']")
    button_place_announcement = (By.XPATH, ".//button[@class='buttonPrimary inButtonText undefined inButtonText']")
    button_logout = (By.XPATH, ".//button[@class='spanGlobal btnSmall']")
    pagination = (By.XPATH, ".//p[@class='spanGlobal']")

class PlaceAnnouncement:

    header_modal_window_without_login = (By.XPATH, ".//div[@class='popUp_titleRow__M7tGg']/h1")
    input_name = (By.XPATH, ".//input[@placeholder='Название']")
    textarea_description = (By.XPATH, ".//textarea[@placeholder='Описание товара']")
    input_price = (By.XPATH, ".//input[@placeholder='Стоимость']")
    button_dropdown_category = (By.XPATH, ".//div[@style='margin: 0px; max-width: 312px; width: 100%;']/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    category_books = (By.XPATH, ".//span[text()='Книги']/parent::button")
    button_dropdown_city = (By.XPATH, ".//div[@style='margin: 0px; max-width: 760px; width: 100%;']/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    city_st_petersburg = (By.XPATH, ".//span[text()='Санкт-Петербург']/parent::button")
    radiobutton_bu = (By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']") 
    button_publish = (By.XPATH, ".//button[text()='Опубликовать']")

class PersonalАccount:
    header_my_announcement = (By.XPATH, ".//h1[text()='Мои объявления']")
    name_last_announcement = (By.XPATH, ".//div[@class='card'][last()]//div[@class='about']//h2")