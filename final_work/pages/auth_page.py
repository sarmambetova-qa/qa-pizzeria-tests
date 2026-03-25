import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from final_work.pages.base_page import BasePage


class AuthPage(BasePage):
    """Страница авторизации и регистрации"""

    url = "https://pizzeria.skillbox.cc/my-account/"

    @allure.step("Открыть страницу авторизации")
    def open_auth_page(self, driver):
        driver.get(self.url)
        time.sleep(2)

    @allure.step("Нажать кнопку 'Зарегистрироваться' и перейти на страницу регистрации")
    def go_to_register_page(self, driver):
        """Нажимает кнопку 'Зарегистрироваться' на странице /my-account/"""
        register_btn = driver.find_element(By.CSS_SELECTOR, "button.custom-register-button")
        register_btn.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/register/")
        )
        time.sleep(1)

    @allure.step("Зарегистрировать нового пользователя: {username}, {email}")
    def register(self, driver, username, email, password):
        """Заполнение формы регистрации на странице /register/"""
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "reg_username"))
        )
        driver.find_element(By.ID, "reg_username").send_keys(username)
        driver.find_element(By.ID, "reg_email").send_keys(email)
        driver.find_element(By.ID, "reg_password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[name='register']").click()
        time.sleep(3)

    @allure.step("Войти в аккаунт: {username}")
    def login(self, driver, username, password):
        """Вход в аккаунт"""
        driver.get("https://pizzeria.skillbox.cc/my-account/")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[name='login']").click()
        time.sleep(3)

    @allure.step("Проверить, что пользователь залогинен")
    def is_logged_in(self, driver):
        """Проверка, что пользователь залогинен (есть меню аккаунта)"""
        # Переходим на страницу аккаунта
        driver.get("https://pizzeria.skillbox.cc/my-account/")
        time.sleep(2)
        try:
            # Ищем меню аккаунта (появляется только для авторизованных)
            menu = driver.find_element(By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation")
            return menu.is_displayed()
        except:
            return False


