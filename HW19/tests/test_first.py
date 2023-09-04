from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logo = 'img.lnXdpd'  # selector
input = '//*[@id="APjFqb"]'

button = '[data-ved="0ahUKEwjbofCQ-PWAAxX1hP0HHeY2BkQQ4dUDCAk"]'
class TestGoogle:

    def test_open_page(self, driver):

        driver.get('https://www.google.com/')

        locator_logo = driver.find_element(By.CSS_SELECTOR, logo)

        driver.save_screenshot('open_google_page.jpg')
        assert WebDriverWait(driver, 5).until(EC.visibility_of(locator_logo))

# Завершение дз 19( лекция 19 время 2:30) создать конфиг, фото в телефоне туда поместить фикстуру, далее в тесте создать файл с тем что она пишет