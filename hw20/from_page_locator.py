from selenium import webdriver
from selenium.webdriver.common.by import By
class FormPageLocators_task1():
    USERNAME_LOCATOR = (By.XPATH, "//input[@name='username']")
    PASSWORD_LOCATOR = "//input[@type='password']"
    BUTTON_LOCATOR = "//input[@type='button']"
    NAME = "Aleesyyya"
    PASSWORD = "qwertt"

class FormPageLocators_task2():
    FIRST_NAME = "Alesya"
    LAST_NAME = "Lukas"
    PHONE = "80292343356"
    EMAIL = "Lukashev@gmail.com"
    ADDRESS = "Moskoyskaya, 17"
    CITY = "Minsk"
    PROVINCE = "Uruchcha"
    POSTAL_CODE = "234567"
    COUNTRY = "Belarus"
    PASSWORD = "qwert"
    first_name_locator = '[name="firstName"]'
    last_name_locator = '[name="lastName"]'
    phone_locator = '[name="phone"]'
    email_locator = '[name="email"]'
    address_locator = '[name="address1"]'
    city_locator = '[name="city"]'
    state_province_locator = '[name="state"]'
    postal_code_locator = '[name="postalCode"]'
    country_select_locator = '[name="country"]'
    user_name_locator = '[name="email"]'
    password_locator = '[name="password"]'
    confirm_password_locator = '[name="confirmPassword"]'
    submit = '[name="submit"]'
    name_check = "//b[contains(text(),'Alesya')]"
    nick_name_check = "//b[contains(text(),'Lukas')]"

class FormPageLocators_test21vek():
    cookie_locator = "//*[@id='modal-cookie']/div/div[2]/div/button[3]/div"
    price_with_discount = "//*[@id='j-item-buyzone']/div[2]/span[1]/span[2]"
    price_without_discount = "//*[@id='j-item-buyzone']/div[2]/span[1]/span[1]"
    all_promotions_locator = "//div[@class='styles_promoItem__aolWq']//a[@href='/special_offers/promo.html']"
    product_locator = "//*[@id='6241841']/div/a/div"
    login_locator = "//span[@class='userToolsText']"
    login_button = "//button[@data-testid='loginButton']"
    regestration_button_locator = "//div[@class='Button-module__buttonText' and text()='Регистрация']"
    emai_locator = "//input[@type='text' and @label='Электронная почта']"
    countinue_button_locator = "//div[@class='Button-module__buttonText' and text()='Продолжить']"
    obrabotka_locator = "//div[@class='Button-module__buttonText' and text()='Соглашаюсь']"
    success_message_locator = "//*[@id='default-modal']/div/div/div[2]/div/div/div/div/h5"
    locator_holodilnik = "//a[@href='/refrigerators/']"
    city_locator = "//button[@type='button' and @class='styles_localityBtn__qrGFQ']"
    populated_place_locator = "//input[@label='Населенный пункт']"
    save_button_locator = "//div[@class='Button-module__buttonText' and text()='Сохранить']"
    but_close_locator = "//button[@type='button' and @tabindex='-1' and @class='style_clearBtn__OGU2X']"
    select_city_from_list = "// li[ @ role = 'row'] / div[text() = 'Гродно']"
    choose_city_locator = "//button[contains(text(),'Гродно')]"