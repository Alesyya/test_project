import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()