# 1. Открыйть сайт http://thedemosite.co.uk/login.php
# 2. Ввести имя в поле username
# 3. Ввести пароль в поле password
# 4. Нажать на кнопку Test Login
# 5. Проверить, что Successful Login отображаются
from selenium.webdriver.common.by import By


from hw20.from_page_locator import FormPageLocators_task1


class Testing(FormPageLocators_task1):
    def test_1(self, driver):
        driver.get("http://thedemosite.co.uk/login.php")

        driver.find_element(By.XPATH, FormPageLocators_task1.USERNAME_LOCATOR).send_keys(FormPageLocators_task1.NAME)
        driver.find_element(By.XPATH, FormPageLocators_task1.PASSWORD_LOCATOR).send_keys(FormPageLocators_task1.PASSWORD)
        driver.find_element(By.XPATH, FormPageLocators_task1.BUTTON_LOCATOR).click()

#текст успешного ввода не получилось проверить так как проблемы со входом, ничего не отображается.