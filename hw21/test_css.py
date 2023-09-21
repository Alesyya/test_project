from selenium.webdriver.common.by import By
from base import wait_for_clicable_by_css_celector


picture_locator = "a.block-link__overlay-link[href='/news/live/world-66851939']"
symbol_bbc_locator = "div[class='orb-nav-section orb-nav-blocks'] [href='https://www.bbc.com']"
sport_locator = "nav[class='orbit-header-links international'] a[href='https://www.bbc.com/sport']"
home_locator = "li[class*='nav__wide-menuitem-container'] span[aria-hidden='true']"
climate_locator = "li[class*='nav__wide-menuitem-container'] [href='/news/science-environment-56837908']"
world_locator = "li[class*='nav__wide-menuitem-container'] [href='/news/world']"

def test_1(driver):
    driver.get('https://www.bbc.com/')

    wait_for_clicable_by_css_celector(driver, picture_locator)
    element = driver.find_element(By.CSS_SELECTOR, picture_locator)

    assert element.is_displayed() == True


def test_2(driver):
    driver.get('https://www.bbc.com/')

    wait_for_clicable_by_css_celector(driver, symbol_bbc_locator)
    element_bbc = driver.find_element(By.CSS_SELECTOR, symbol_bbc_locator)

    assert element_bbc.is_displayed() == True


def test_3(driver):
    driver.get('https://www.bbc.com/')

    wait_for_clicable_by_css_celector(driver, sport_locator)
    element_sport = driver.find_element(By.CSS_SELECTOR, sport_locator)

    assert element_sport.is_displayed() == True


def test_4(driver):
    driver.get('https://www.bbc.com/news')

    wait_for_clicable_by_css_celector(driver, home_locator)
    element_home = driver.find_element(By.CSS_SELECTOR, home_locator)

    assert element_home.is_displayed() == True


def test_5(driver):
    driver.get('https://www.bbc.com/news')

    wait_for_clicable_by_css_celector(driver, climate_locator)
    element_climate = driver.find_element(By.CSS_SELECTOR, climate_locator)

    assert element_climate.is_displayed() == True


def test_6(driver):
    driver.get('https://www.bbc.com/news')

    wait_for_clicable_by_css_celector(driver, world_locator)
    element_world = driver.find_element(By.CSS_SELECTOR, world_locator)

    assert element_world.is_displayed() == True