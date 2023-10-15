#тест на закрытие окна куки(принятие)
#тест на проверку перечня товаров на акции
#тест на проверку того, что при нажатии на кнопку холодильники открываются дествительно холодильники
#тест на проверку изменения города доставки заказа
#тест на регистрацию или вход
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from hw20.from_page_locator import FormPageLocators_test21vek


class Testing1(FormPageLocators_test21vek):
    def test_1(self, driver):
        """
        test for checking the main title
        """
        driver.get("https://www.21vek.by/")
        assert driver.title == "Онлайн-гипермаркет 21vek.by"


    def test_2(self, driver):
        """
        checking whether there is a discount on a product that is on sale
        """
        driver.get('https://www.21vek.by/')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.cookie_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.cookie_locator).click()

        driver.find_element(By.XPATH, FormPageLocators_test21vek.all_promotions_locator).click()
        driver.find_element(By.XPATH, FormPageLocators_test21vek.product_locator).click()

        higher_price1 = driver.find_element(By.XPATH, FormPageLocators_test21vek.price_without_discount)
        lower_price2 = driver.find_element(By.XPATH, FormPageLocators_test21vek.price_with_discount)
        higher_price = float(re.sub('[^0-9.]', '', higher_price1.text))
        lower_price = float(re.sub('[^0-9.]', '', lower_price2.text))

        if higher_price > lower_price:
            print("Цена снижена")
        elif higher_price < lower_price:
            print("Цена не снижена")
        else:
            print("Цены равны")

        assert higher_price > lower_price, 'Цена снижена'


    def test_3(self, driver):
        """
        checking that when the button is pressed, the refrigerators actually open
        """
        driver.get("https://www.21vek.by/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.cookie_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.cookie_locator).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.locator_holodilnik)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.locator_holodilnik).click()

        items = driver.find_elements(By.XPATH, "//div[@class='catalog']//div[contains(@class, 'item__title') and contains(text(),'Холодильник')]")
        assert len(items) == len(driver.find_elements(By.XPATH, "//div[@class='catalog']//div[contains(@class, 'item__title')]"))

    def test_4(self, driver):
        """
        checking the operation of registration
        """
        driver.get('https://www.21vek.by/')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.cookie_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.cookie_locator).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.login_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.login_locator).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.login_button)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.login_button).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.regestration_button_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.regestration_button_locator).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.emai_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.emai_locator).send_keys('uyuyo@gmail.com')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.countinue_button_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.countinue_button_locator).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.obrabotka_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.obrabotka_locator).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, FormPageLocators_test21vek.success_message_locator)))
        assert driver.find_element(By.XPATH, FormPageLocators_test21vek.success_message_locator).text == "Вы зарегистрированы"

    def test_5(self, driver):
        """
        check changes in the order delivery city
        """
        driver.get('https://www.21vek.by/')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.cookie_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.cookie_locator).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.city_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.city_locator).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, FormPageLocators_test21vek.populated_place_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.but_close_locator).click()

        driver.find_element(By.XPATH, FormPageLocators_test21vek.select_city_from_list).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FormPageLocators_test21vek.save_button_locator)))
        driver.find_element(By.XPATH, FormPageLocators_test21vek.save_button_locator).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, FormPageLocators_test21vek.choose_city_locator)))
        assert driver.find_element(By.XPATH, FormPageLocators_test21vek.choose_city_locator).text == 'г. Гродно'




