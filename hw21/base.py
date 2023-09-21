from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_clicable_by_xpath(driver, locator):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))


def wait_for_clicable_by_css_celector(driver, locator):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))


def wait_for_element_is_displayed(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    if element.is_displayed():
        return True
    else:
        return print("Element is  not displayed")


def wait_for_element_is_enabled(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    if element.is_enabled():
        return True
    else:
        return print("Element is  not enabled")

def get_attribute(driver, locator, name):
    element = driver.find_element(By.XPATH, locator)
    element.get_attribute(name)


def check_checkbox(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    element.click()


def uncheck_checkbox(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    if element.is_selected():
        element.click()
    else:
        print("Choose another")


def inputs_text(driver, locator, text):
    element = driver.find_element(By.XPATH, locator).click()
    element.send_keys(text)


def test_dropdown(driver, locator, value):
    element = Select(driver.find_element(By.XPATH, locator))
    element.select_by_value(value)


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, window.innerHeight);")


def check_radio_button(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    element.click()
