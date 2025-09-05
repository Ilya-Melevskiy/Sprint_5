import pytest

from selenium import webdriver

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()


