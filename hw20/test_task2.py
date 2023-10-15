# 1. Открыть сайт http://demo.guru99.com/test/newtours/register.php
# 2. Заполнить все поля
# 3. Нажать кнопку Submit
# 4. Проверить, что отображается правильно имя и фамилия
# 5.Проверить, что отображается правильно username
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from hw20.from_page_locator import FormPageLocators_task2


class Testing_2():
    def test_1(self, driver):
        driver.get('http://demo.guru99.com/test/newtours/register.php')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, FormPageLocators_task2.first_name_locator)))
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.first_name_locator).send_keys(FormPageLocators_task2.FIRST_NAME)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.last_name_locator).send_keys(FormPageLocators_task2.LAST_NAME)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.phone_locator).send_keys(FormPageLocators_task2.PHONE)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.email_locator).send_keys(FormPageLocators_task2.EMAIL)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.address_locator).send_keys(FormPageLocators_task2.ADDRESS)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.city_locator).send_keys(FormPageLocators_task2.CITY)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.state_province_locator).send_keys(FormPageLocators_task2.PROVINCE)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.postal_code_locator).send_keys(FormPageLocators_task2.POSTAL_CODE)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.country_select_locator).send_keys(FormPageLocators_task2.COUNTRY)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.user_name_locator).send_keys(FormPageLocators_task2.FIRST_NAME)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.password_locator).send_keys(FormPageLocators_task2.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.confirm_password_locator).send_keys(FormPageLocators_task2.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.email_locator).send_keys(FormPageLocators_task2.EMAIL)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.submit).click()
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, FormPageLocators_task2.name_check)))


    def test_2(self, driver):
        driver.get('http://demo.guru99.com/test/newtours/register.php')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, FormPageLocators_task2.first_name_locator)))
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.first_name_locator).send_keys(FormPageLocators_task2.FIRST_NAME)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.last_name_locator).send_keys(FormPageLocators_task2.LAST_NAME)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.phone_locator).send_keys(FormPageLocators_task2.PHONE)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.email_locator).send_keys(FormPageLocators_task2.EMAIL)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.address_locator).send_keys(FormPageLocators_task2.ADDRESS)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.city_locator).send_keys(FormPageLocators_task2.CITY)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.state_province_locator).send_keys(FormPageLocators_task2.PROVINCE)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.postal_code_locator).send_keys(FormPageLocators_task2.POSTAL_CODE)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.country_select_locator).send_keys(FormPageLocators_task2.COUNTRY)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.user_name_locator).send_keys(FormPageLocators_task2.FIRST_NAME)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.password_locator).send_keys(FormPageLocators_task2.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.confirm_password_locator).send_keys(FormPageLocators_task2.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.email_locator).send_keys(FormPageLocators_task2.EMAIL)
        driver.find_element(By.CSS_SELECTOR, FormPageLocators_task2.submit).click()
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, FormPageLocators_task2.nick_name_check)))
