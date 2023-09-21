from selenium.webdriver.common.by import By
from base import wait_for_clicable_by_xpath


picture_locator = "//a[@class='block-link__overlay-link' and @href='/news/live/world-66851939']"
symbol_bbc_locator = "//a[@href='https://www.bbc.com']"
sport_locator = "//header[@id='orb-banner']//a[@href='https://www.bbc.com/sport']//span[text()='Sport']"
home_locator = "//div[starts-with(@class, 'gs-u-d')]//a[@href='/news']"
climate_locator = "//div[starts-with(@class, 'gs-u-d')]//span[text()='Climate']"
world_locator = "//div[starts-with(@class, 'gs-u-d')]//span[text()='World']"

def test_1(driver):
    driver.get('https://www.bbc.com/')

    wait_for_clicable_by_xpath(driver, picture_locator)
    element = driver.find_element(By.XPATH, picture_locator)

    assert element.is_displayed() == True


def test_2(driver):
    driver.get('https://www.bbc.com/')

    wait_for_clicable_by_xpath(driver, symbol_bbc_locator)
    element_bbc = driver.find_element(By.XPATH, symbol_bbc_locator)

    assert element_bbc.is_displayed() == True


def test_3(driver):
    driver.get('https://www.bbc.com/')

    wait_for_clicable_by_xpath(driver, sport_locator)
    element_sport = driver.find_element(By.XPATH, sport_locator)

    assert element_sport.is_displayed() == True



def test_4(driver):
    driver.get('https://www.bbc.com/news')

    wait_for_clicable_by_xpath(driver, home_locator)
    element_home = driver.find_element(By.XPATH, home_locator)

    assert element_home.is_displayed() == True


def test_5(driver):
    driver.get('https://www.bbc.com/news')

    wait_for_clicable_by_xpath(driver, climate_locator)
    element_climate = driver.find_element(By.XPATH, climate_locator)

    assert element_climate.is_displayed() == True


def test_6(driver):
    driver.get('https://www.bbc.com/news')

    wait_for_clicable_by_xpath(driver, world_locator)
    element_world = driver.find_element(By.XPATH, world_locator)

    assert element_world.is_displayed() == True



